from django.contrib.auth.views import login, logout
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response
from django.contrib.auth.models import User
from django.template import RequestContext
from django.contrib.auth import authenticate
from django.views.generic.simple import direct_to_template

from coordi.base.forms import SignupForm, WallPostForm, WallCommentForm
from coordi.base.models import UserProfile, Promocode, Post, Comment, Photo
from coordi.showcase.models import Theme, Album, Showcase
'''
def find_codi(name):
    return find_customuser(name).codi

def find_customuser(name):
    return UserProfile.objects.get(user__username = name)

def find_user(name):
    return User.objects.get(username = name)
''' 

def custom_login(request):
    print 'accessing auth/custom_login...'
    
    if request.user.is_authenticated():
        return HttpResponseRedirect('/')
    else:
        return login(request)

@login_required
def custom_logout(request):
    print 'accessing auth/custom_logout...'
    return logout(request)

def signup(request):
    print 'accessing auth/singup...'
    if request.user.is_authenticated():
        return HttpResponseRedirect('/')
    else:
        if request.method == 'POST':
            form = SignupForm(request.POST, request.FILES)

            if form.is_valid():
                cd = form.cleaned_data
                print 'cd', cd
                print request.FILES

                new_user = User.objects.create_user(cd['username'], cd['email'], cd['password'])
                new_user.first_name = cd['first_name']
                new_user.last_name = cd['last_name']
                
                try:
                    promocode = Promocode.objects.get(promocode_id = cd['promocode'])
                    for permission in promocode.permissions.all():
                        new_user.user_permissions.add(permission)
                        if permission.content_type.app_label == 'showcase'\
                        and permission.content_type.model == 'theme':
                            new_showcase = Showcase.objects.filter().order_by('-episode_id')[0]
                            new_album = Album(coordi = new_user,
                                theme = Theme.objects.get(theme_pos = permission.codename,
                                showcase = new_showcase))
                            new_album.save()

                    Promocode.objects.get(promocode_id = cd['promocode']).delete()
                except Promocode.DoesNotExist:
                    pass
                new_user.save()
                
                new_image = cd['photo']
                if new_image is not None:
                    print 'not none!'
                    photo = Photo(image = new_image)
                    photo.save()
                    new_user.get_profile().photo = photo
                    new_user.get_profile().save()
                else:
                    print 'no photo :/'
                return HttpResponseRedirect('/signup/thanks/')
        else:
            form = SignupForm(
               initial={'password' : '',
                        'password2' : 'repeat password',
                        'email' : '@',
                        'email2' : 'repeat email'}
            )
    return render_to_response('registration/signup.html', {'form': form}, context_instance = RequestContext(request))
def signup_thanks(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect('/')
    else:
        return render_to_response('registration/signup_thanks.html', context_instance = RequestContext(request))

def main(request):
    #if request.user.is_authenticated():
    #    return HttpResponseRedirect('/home/')
    #else:
    return render_to_response('base/main.html', context_instance = RequestContext(request))

def how_it_works(request):
    return render_to_response('base/how_it_works.html', context_instance = RequestContext(request))



@login_required
def post(request, id):
    try:
        requested = Post.objects.get(post_id = id)
    except Post.DoesNotExist:
        return render_to_response('base/http404.html', context_instance = RequestContext(request))
    
    if request.method == 'POST':
        print 'post?'
        form = WallCommentForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            print 'valid?', cd['comment']

            custom_user = UserProfile.objects.get(user__username = request.user.username)
            Comment(message = cd['comment'], owner = custom_user, post = requested).save()

    comments = Comment.objects.filter(post=requested).order_by('-time_created')
    return render_to_response('post.html', {'form' : WallCommentForm(), 'post' : requested, 'comments' : comments,  'codi' : requested.owner}, context_instance = RequestContext(request))

@login_required
def codi_wall(request, codi_id, garbage):
    codi = None#codi = get_customuser(request, codi_id)
    form = None
    is_page_owner = False
    
    if request.user.username == codi_id:
        is_page_owner = True
        if request.method == 'POST':
        
            form = WallPostForm(request.POST)
            if form.is_valid():
                cd = form.cleaned_data
                Post(message = cd['post'], owner = codi).save()
                
    posts = Post.objects.filter(owner = codi).order_by('-time_modified')
    print is_page_owner
    print WallPostForm().as_ul()
    return render_to_response('codi_wall.html', {'codi' : codi, 'form' : WallPostForm(), 'is_page_owner' : is_page_owner, 'posts' : posts}, context_instance = RequestContext(request))
'''
@login_required
def album(request, id):
    try:
        requested = Album.objects.get(album_id = id)
    except Album.DoesNotExist:
        return render_to_response('http404.html', context_instance = RequestContext(request))
    photos = Photo.objects.filter(album=requested).order_by('position')
    requested.all_visit += 1
    requested.save()
    return render_to_response('album.html', {'photos' : photos, 'codi' : requested.owner, 'album' : requested}, context_instance = RequestContext(request))
'''