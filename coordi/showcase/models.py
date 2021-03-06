from django.db import models
from django.contrib.auth.models import User, Permission
import os, os.path
from binascii import hexlify
from coordi.base.models import Photo, _createId

# Create your models here.
class Showcase(models.Model):
    showcase_id = models.CharField(max_length=32, primary_key=True, default=_createId)
    
    '''
    time_vote_start = models.DateTimeField()
    time_vote_end = models.DateTimeField()
    time_upload_start = models.DateTimeField()
    time_upload_end = models.DateTimeField()
    '''
    is_votable = models.BooleanField(default = False)
    is_editable = models.BooleanField(default = False)
    is_viewable = models.BooleanField(default = False)
    is_closed = models.BooleanField(default = False)
    #Phase of an album
    # is_editable -> is_closed -> is_votable -> is_viewable
    episode_id = models.PositiveSmallIntegerField(unique = True)
    def __unicode__(self):
        return 'Episode %s'% self.episode_id

class Theme(models.Model):
    theme_id = models.CharField(max_length=32, primary_key=True, default=_createId)
    showcase = models.ForeignKey(Showcase)
    keyword = models.CharField(max_length=10)
    subject = models.CharField(max_length=100)
    theme_pos = models.PositiveSmallIntegerField()
    class Meta:
        permissions = (
            ("1", "Can work on theme 1."),
            ("2", "Can work on theme 2."),
            ("3", "Can work on theme 3."),
            ("4", "Can work on theme 4."),
            ("5", "Can work on theme 5."),
            ("6", "Can work on theme 6."),
            ("7", "Can work on theme 7."),
            ("8", "Can work on theme 8."),
        )
    def __unicode__(self):
        return 'Episode %s Theme %s' % (self.showcase.episode_id, self.theme_pos)

class Album(models.Model):
    album_id = models.CharField(max_length=32, primary_key=True, default=_createId)
    theme = models.ForeignKey(Theme)
    coordi = models.ForeignKey(User)
    title = models.CharField(max_length=50, default = u'Untitled')

class Unlock(models.Model):
    theme = models.ForeignKey(Theme)
    voter = models.OneToOneField(User)

class Vote(models.Model):
    album = models.ForeignKey(Album)
    voter = models.ForeignKey(User)

from django import template
register = template.Library()

def is_voted(theme, user):
    return Vote.objects.filter(voter = user, album__theme = theme).exists()
def count_votes(new_album):
    return Vote.objects.filter(album=new_album).count()
register.filter('is_voted', is_voted)
register.filter('count_votes', count_votes)

class Entry(models.Model):
    entry_id = models.CharField(max_length=32, primary_key=True, default=_createId)
    album = models.ForeignKey(Album)
    entry_pos = models.PositiveSmallIntegerField()
    text = models.CharField(max_length=100, blank = True, null = True)
    photo = models.OneToOneField(Photo)
    
    def __unicode__(self):
        return 'Album: %s, Entry Position: %s' %(self.album.title, self.entry_pos)
