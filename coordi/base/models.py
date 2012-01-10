from django.db import models
from django.contrib.auth.models import User, Permission
from django.db.models.signals import post_save

import os, os.path
from binascii import hexlify
import datetime

def _createId():
    return hexlify(os.urandom(16))

def _createPhotoPath(instance, filename):
    return os.path.join('photo', instance.photo_id)

class Promocode(models.Model):
    promocode_id = models.CharField(max_length = 35, default = _createId, unique = True)
    permissions = models.ManyToManyField(Permission)
class Photo(models.Model):
    photo_id = models.CharField(max_length=32, primary_key=True, default=_createId)
    #title = models.CharField(max_length=30)#, min_length = 4)
    image = models.ImageField(upload_to = _createPhotoPath)

'''Points use notification system like that of Stackoverflow.com '''
class UserProfile(models.Model):
    #user_id = models.CharField(max_length = 20, primary_key = True)
    #profile_photo = models.ImageField(upload_to=os.path.join(os.path.dirname(__file__), 'photo/codi/%d'%codi_id))
    user = models.OneToOneField(User)
    #codi = models.OneToOneField(Codi, null = True, blank = True)
    accum_point = models.IntegerField(default = 0)
    accum_cach = models.IntegerField(default = 0)
    point = models.IntegerField(default = 0)
    cash = models.IntegerField(default = 0)
    photo = models.OneToOneField(Photo, blank = True, null = True)
    level = models.PositiveSmallIntegerField(default = 1)
    #accum_votes = models.PositiveIntegerField(default = 0)
    #required_votes = models.PositiveIntegerField(default = SHOWCASE_VOTES)
    #other = models.ManyToManyField('self', through = 'Message')
    
    #profile_photo = models.OneToOneField(Photo, unique = True)
    #messages = models
    #def vote(self):
    #    self.accum_votes += 1
    #    self.required_votes -= 1

    def __unicode__(self):
        return '%s %s' % (self.user.first_name, self.user.last_name)


def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

post_save.connect(create_user_profile, sender=User)




class Message(models.Model):
    content = models.TextField(max_length = 500)
    time = models.DateTimeField(auto_now_add = True)
    sender_id = models.CharField(max_length = 30)
    recipient_id = models.CharField(max_length = 30)

class Post(models.Model):
    post_id = models.CharField(max_length=32, primary_key=True, default=_createId)
    owner = models.ForeignKey(UserProfile)
    message = models.TextField(max_length=500)
    time_created = models.DateTimeField(auto_now_add = True, default=datetime.date.today())
    time_modified = models.DateTimeField(auto_now = True, default=datetime.date.today())
    unique_visit = models.PositiveIntegerField(default = 1)
    all_visit = models.PositiveIntegerField(default = 1)

    def __unicode__(self):
        return self.owner.user.get_full_name()

class Comment(models.Model):
    comment_id = models.CharField(max_length=32, primary_key=True, default=_createId)
    #title = models.CharField(max_length=30)#, min_length = 4)
    owner = models.ForeignKey(UserProfile)

    message = models.TextField(max_length=100)
    time_created = models.DateTimeField(auto_now_add = True, default=datetime.date.today())
    time_modified = models.DateTimeField(auto_now = True, default=datetime.date.today())

    post = models.ForeignKey(Post)
    
    def __unicode__(self):
        return '%s' %(self.post.owner)

    