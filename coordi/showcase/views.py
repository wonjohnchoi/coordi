# Create your views here.

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.db.models import Q
from collections import OrderedDict

from django.contrib.auth.models import Permission
from coordi.showcase.models import Showcase, Theme, Vote, Album, Unlock, Entry, Photo
from coordi.showcase.forms import EntryForm
import datetime
def get_voting_showcase():
    showcases = Showcase.objects().filter(Q(time_vote_start__lte = datetime.date.today()) & Q(time_vote_end__gte = datetime.date.today()))
    if not showcases.exists():
        return None
    if showcases.count() != 1:
        raise Exception('Fatal: There are multiple showcases in voting period')
    return showcases[0]
def get_uploading_showcase():
    showcases = Showcase.objects().filter(Q(time_upload_start__lte = datetime.date.today()) & Q(time_upload_end__gte = datetime.date.today()))
    if not showcases.exists():
        return None
    if showcases.count() != 1:
        raise Exception('Fatal: There are multiple showcases in uploading period')
    return showcases[0]

@login_required
def voting_showcase(request):
    episode_id = get_voting_showcase().episode_id
    return HttpResponseRedirect('/showcase/%d/'% episode_id)
@login_required
def uploading_showcase(request):
    episode_id = get_uploading_showcase().episode_id
    return HttpResponseRedirect('/showcase/%d/'% episode_id)


@login_required
def showcase(request, new_episode_id):
    print 'accessing showcase/showcase'
    try:
        new_showcase = Showcase.objects.get(episode_id = int(new_episode_id))
    except Showcase.DoesNotExist:
        return render_to_response('base/http404.html', context_instance = RequestContext(request))
        
    theme_queryset = new_showcase.theme_set.all().order_by('theme_pos')
    themeProfiles = []

    try:
        unlocked = Unlock.objects.get(voter = request.user, theme__showcase = new_showcase)
        unlocked_theme = unlocked.theme
    except Unlock.DoesNotExist:
        unlocked = None
        unlocked_theme = None
    if request.method == 'POST':
        if 'unlock' in request.POST and not unlocked:
            try:
                unlocked_theme = theme_queryset.get(theme_id = request.POST['unlock'])                                
                unlocked = Unlock(theme = unlocked_theme, voter = request.user).save()
                
            except Theme.DoesNotExist:
                pass
        elif 'vote' in request.POST and unlocked:
            try:
                voted = Album.objects.get(album_id = request.POST['vote'], theme__showcase = new_showcase)
                if voted.theme == unlocked.theme:
                    Vote(album = voted, voter = request.user).save()
                    Unlock.objects.filter(theme__showcase = new_showcase).delete()
                    unlocked_theme = None
            except Album.DoesNotExist:
                pass

    votes = Vote.objects.filter(album__theme__showcase = new_showcase)
    for theme in theme_queryset:
        profile = {}
        profile['is_voted'] = Vote.objects.filter(voter = request.user, album__theme = theme).exists()
        profile['theme_id'] = theme.theme_id
        profile['keyword'] = theme.keyword
        profile['subject'] = theme.subject

        if theme == unlocked_theme or profile['is_voted']:
            albums = sorted(theme.album_set.all(), key=lambda new_album:votes.filter(album = new_album).count(), reverse = True)
        else:
            albums = theme.album_set.all()
        profile['albums'] = albums
        themeProfiles.append(profile)
    if theme_queryset.exists():
        max_albums = max(theme.album_set.count() for theme in theme_queryset)
    else:
        max_albums = 0
    print unlocked
    return render_to_response('showcase/showcase.html', {'themes': themeProfiles, 'max_albums' : range(max_albums), 'unlocked' : unlocked_theme}, context_instance = RequestContext(request))

@login_required
def album(request, new_album_id):
    try:
        album = Album.objects.get(album_id = new_album_id)
    except Album.DoesNotExist:
        return render_to_response('base/http404.html', context_instance = RequestContext(request))
    #albums = album.coordi.album_set.all().order_by('-theme__showcase__time_start')
    entries = album.entry_set.all().order_by('entry_pos')

    return render_to_response('showcase/album.html', {'coordi':album.coordi, 'album': album, 'entries' : entries}, context_instance = RequestContext(request))

@login_required
def workspace(request, new_theme_pos):
    new_showcase = Showcase.objects.filter().order_by('-episode_id')[0]
    new_theme = Theme.objects.get(showcase = new_showcase, theme_pos = new_theme_pos)
    print 'episode_id', new_showcase.episode_id, 'theme Position', new_theme_pos


    

    if not request.user.has_perm(u'showcase.%s'%new_theme_pos):
        return render_to_response('base/http404.html', context_instance = RequestContext(request))
    
    #TODO title
    entry_form = None
    

    new_album = Album.objects.get(coordi = request.user, theme = new_theme)
    
    entries = Entry.objects.filter(album = new_album).order_by('entry_pos')
    count = entries.count()
    print 'count', count
    if request.method == 'POST':
        entry_form = EntryForm(request.POST, request.FILES)
        print request.POST
        print request.FILES
        print 'valid?'
        if entry_form.is_valid():
            print 'valid!'
            cd = entry_form.cleaned_data
            print 'cd', cd
            print request.FILES
            if 'plus' in request.POST:
                
                new_entry_pos = int(request.POST['plus'])
                print 'entry position: ', new_entry_pos
                if 1 <= new_entry_pos <= count + 1:
                    if new_entry_pos != count + 1:
                        for pos in range(count, new_entry_pos - 1, -1):
                            entry = entries.get(entry_pos = unicode(pos))
                            print 'moving entry #', pos, 'forward'
                            entry.entry_pos = unicode(pos + 1)
                            entry.save()
                    new_photo = Photo(image = cd['photo'])
                    new_photo.save()
                    Entry(entry_pos = unicode(new_entry_pos), album = new_album, text = cd['text'], photo = new_photo).save()
                    entry_form = None           
        if 'minus' in request.POST:
            new_entry_pos = int(request.POST['minus'])
            if 1 <= new_entry_pos <= count:
                entry = entries.get(entry_pos = request.POST['minus'])
                entry.delete()
                print 'deleting entry #', new_entry_pos
                
                for pos in range(new_entry_pos + 1, count + 1):
                    print 'moving backward entry post of entry #', pos
                    entry = entries.get(entry_pos = unicode(pos))
                    entry.entry_pos = unicode(pos - 1)
                    entry.save()
        print request.POST
        if 'title' in request.POST:
            
            new_album.title = request.POST['title']
            new_album.save()
    if entry_form is None:
        entry_form = EntryForm(initial={'text':'Describe this photo'})#, prefix = 'create_entry')
    if request.method == 'POST':
        entries = Entry.objects.filter(album = new_album).order_by('entry_pos')

    return render_to_response('showcase/workspace.html', {'coordi':new_album.coordi, 'entry_form': entry_form, 'album' : new_album, 'entries' :entries}, context_instance = RequestContext(request))
        
