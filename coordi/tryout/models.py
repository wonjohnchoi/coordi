from django.db import models
from django.contrib.auth.models import User, Permission
import os, os.path
from binascii import hexlify
from coordi.base.models import Photo, _createId

class Tryout(models.Model):
    tryout_id = models.CharField(max_length=32, primary_key=True, default=_createId)
    is_votable = models.BooleanField(default = False)
    is_editable = models.BooleanField(default = False)
    is_viewable = models.BooleanField(default = False)

class Album(models.Model):
    album_id = models.CharField(max_length=32, primary_key=True, default=_createId)
    tryout = models.ForeignKey(Tryout)
    coordi = models.ForeignKey(User)
    title = models.CharField(max_length=50, default = u'Untitled')
    keyword = models.CharField(max_length=5, default = u'keyword')
    text = models.CharField(max_length=100, blank = True, null = True, default='Explain album.')
    
    
'''Only users with enough points shall vote.'''
class Vote(models.Model):
    album = models.ForeignKey(Album)
    voter = models.ForeignKey(User)

class Entry(models.Model):
    entry_id = models.CharField(max_length=32, primary_key=True, default=_createId)
    album = models.ForeignKey(Album)
    entry_pos = models.PositiveSmallIntegerField()
    photo = models.OneToOneField(Photo)
    
    def __unicode__(self):
        return 'Album: %s, Entry Position: %s' %(self.album.title, self.entry_pos)
