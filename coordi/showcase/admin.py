'''
Created on Dec 18, 2011

@author: wonjohnchoi
'''

from django.contrib import admin
from coordi.showcase import models

#admin.site.register(models.Photo)
#admin.site.register(models.TitlePhoto)

#admin.site.register(models.Album)
#admin.site.register(models.Post)
#admin.site.register(models.Comment)
#admin.site.register(models.Theme)
#admin.site.register(models.Vote)
admin.site.register(models.Showcase)
admin.site.register(models.Theme)
admin.site.register(models.Album)
admin.site.register(models.Entry)
admin.site.register(models.Vote)

#admin.site.register(models.Codi)
#admin.site.register(models.Message)
