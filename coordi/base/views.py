from django.contrib.auth.views import login, logout
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response
from django.contrib.auth.models import User
from django.template import RequestContext
from django.contrib.auth import authenticate
from django.views.generic.simple import direct_to_template

from coordi.base.forms import SignupForm
from coordi.base.models import CustomUser
'''
def find_codi(name):
    return find_customuser(name).codi

def find_customuser(name):
    return CustomUser.objects.get(user__username = name)

def find_user(name):
    return User.objects.get(username = name)
''' 

def custom_login(request):
    print 'accessing auth/custom_login...'
    
    if request.user.is_authenticated():
        return HttpResponseRedirect('/')
    else:
        #print authenticate(username = 'kaj011', password = '123123')
        #print authenticate(username = 'wonjohn.choi', password = '2310aa')
        #user = User.objects.get(username='kaj011')
        #print user
        #print user.password
        #print user.check_password('123123')
        

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
            form = SignupForm(request.POST)
            if form.is_valid():
                cd = form.cleaned_data
                new_user = User.objects.create_user(cd['username'], cd['email'], cd['password'])
                new_user.first_name = cd['first_name']
                new_user.last_name = cd['last_name']
                new_user.save()
                CustomUser(user=new_user).save()
                '''                User(
                   username = cd['username'], first_name = cd['first_name'],
                   last_name = cd['last_name'], password = cd['password'],
                   email = cd['email']).save(force_insert = True)'''
            
                return HttpResponseRedirect('/signup/thanks/')
        else:
            form = SignupForm(
               initial={'password' : 'make it hard to guess',
                        'email' : 'email@domain',
                        'email2' : 'repeat yourself'}
            )
    return render_to_response('registration/signup.html', {'form': form}, context_instance = RequestContext(request))
def signup_thanks(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect('/')
    else:
        return render_to_response('registration/signup_thanks.html', context_instance = RequestContext(request))
