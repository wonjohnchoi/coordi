from django.db import models
from django.contrib.auth.models import User, Permission
import os, os.path
from binascii import hexlify
from coordi.base.models import Photo

def _createId():
    return hexlify(os.urandom(16))

def _createPhotoPath(instance, filename):
    return os.path.join('photo', instance.photo_id)
# Create your models here.
class Showcase(models.Model):
    showcase_id = models.CharField(max_length=32, primary_key=True, default=_createId)

    time_start = models.DateTimeField()
    time_end = models.DateTimeField()
    episode_id = models.PositiveSmallIntegerField(unique = True)

class Theme(models.Model):
    theme_id = models.CharField(max_length=32, primary_key=True, default=_createId)
    showcase = models.ForeignKey(Showcase)
    keyword = models.CharField(max_length=10)
    subject = models.CharField(max_length=100)
    theme_pos = models.PositiveSmallIntegerField()


class Album(models.Model):
    album_id = models.CharField(max_length=32, primary_key=True, default=_createId)
    theme = models.ForeignKey(Theme)
    coordi = models.ForeignKey(User)
    title = models.CharField(max_length=50)

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
    text = models.CharField(max_length=100)
    photo = models.OneToOneField(Photo)
    

