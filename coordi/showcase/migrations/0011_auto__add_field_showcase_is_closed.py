# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding field 'Showcase.is_closed'
        db.add_column('showcase_showcase', 'is_closed', self.gf('django.db.models.fields.BooleanField')(default=False), keep_default=False)


    def backwards(self, orm):
        
        # Deleting field 'Showcase.is_closed'
        db.delete_column('showcase_showcase', 'is_closed')


    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'base.photo': {
            'Meta': {'object_name': 'Photo'},
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'photo_id': ('django.db.models.fields.CharField', [], {'default': "'b1b8058b6d9235b1803762d0600670ff'", 'max_length': '32', 'primary_key': 'True'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'showcase.album': {
            'Meta': {'object_name': 'Album'},
            'album_id': ('django.db.models.fields.CharField', [], {'default': "'5a80f92c156749c1c2fe16553dc0ae32'", 'max_length': '32', 'primary_key': 'True'}),
            'coordi': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"}),
            'theme': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['showcase.Theme']"}),
            'title': ('django.db.models.fields.CharField', [], {'default': "u'Untitled'", 'max_length': '50', 'null': 'True', 'blank': 'True'})
        },
        'showcase.entry': {
            'Meta': {'object_name': 'Entry'},
            'album': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['showcase.Album']"}),
            'entry_id': ('django.db.models.fields.CharField', [], {'default': "'4d61713f8ea983abcfa0774a26d5f9a9'", 'max_length': '32', 'primary_key': 'True'}),
            'entry_pos': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'photo': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['base.Photo']", 'unique': 'True'}),
            'text': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'})
        },
        'showcase.showcase': {
            'Meta': {'object_name': 'Showcase'},
            'episode_id': ('django.db.models.fields.PositiveSmallIntegerField', [], {'unique': 'True'}),
            'is_closed': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_editable': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_viewable': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_votable': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'showcase_id': ('django.db.models.fields.CharField', [], {'default': "'571166982def5689b18b2da7cba67deb'", 'max_length': '32', 'primary_key': 'True'})
        },
        'showcase.theme': {
            'Meta': {'object_name': 'Theme'},
            'keyword': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'showcase': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['showcase.Showcase']"}),
            'subject': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'theme_id': ('django.db.models.fields.CharField', [], {'default': "'82ec1ddf07561bc46d7a34825f1e3e34'", 'max_length': '32', 'primary_key': 'True'}),
            'theme_pos': ('django.db.models.fields.PositiveSmallIntegerField', [], {})
        },
        'showcase.unlock': {
            'Meta': {'object_name': 'Unlock'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'theme': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['showcase.Theme']"}),
            'voter': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['auth.User']", 'unique': 'True'})
        },
        'showcase.vote': {
            'Meta': {'object_name': 'Vote'},
            'album': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['showcase.Album']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'voter': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"})
        }
    }

    complete_apps = ['showcase']
