# Create your views here.

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.db.models import Q
from collections import OrderedDict

from coordi.showcase.models import Showcase, Theme, Vote, Album
def redirect_showcase(request):
    episode_id = Showcase.objects.order_by('-episode_id')[0].episode_id
    return HttpResponseRedirect('/showcase/%d'% episode_id)
def showcase(request, new_episode_id):
    print 'accessing showcase/showcase'
    try:
        new_showcase = Showcase.objects.get(episode_id = int(new_episode_id))
    except Showcase.DoesNotExist:
        return render_to_response('base/http404.html', context_instance = RequestContext(request))
    theme_queryset = new_showcase.theme_set.all().order_by('theme_pos')
    themes = []
    votes = Vote.objects.filter(album__theme__showcase = new_showcase)
    for theme in theme_queryset:
        albums = sorted(theme.album_set.all(), key=lambda new_album:votes.filter(album = new_album).count(), reverse = True)

        themes.append({'theme_id':theme.theme_id,'keyword':theme.keyword, 'subject':theme.subject, 'albums' : albums})
        print 'albums', albums
        for album in albums:
            print album.album_id
    max_albums = max(theme.album_set.count() for theme in theme_queryset)
    print 'max_albums:', max_albums
    return render_to_response('showcase/showcase.html', {'themes': themes, 'max_albums' : range(max_albums)}, context_instance = RequestContext(request))
def album(request, new_album_id):
    try:
        album = Album.objects.get(album_id = new_album_id)
    except Album.DoesNotExist:
        return render_to_response('base/http404.html', context_instance = RequestContext(request))
    albums = album.coordi.album_set.all().order_by('-theme__showcase__time_start')
    entries = album.entry_set.all().order_by('entry_pos')
    return render_to_response('showcase/album.html', {'album': album,'albums' : albums, 'entries' : entries}, context_instance = RequestContext(request))