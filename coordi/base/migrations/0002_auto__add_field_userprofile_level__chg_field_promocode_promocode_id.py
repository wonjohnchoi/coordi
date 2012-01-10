# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding field 'UserProfile.level'
        db.add_column('base_userprofile', 'level', self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=1), keep_default=False)

        # Changing field 'Promocode.promocode_id'
        db.alter_column('base_promocode', 'promocode_id', self.gf('django.db.models.fields.CharField')(unique=True, max_length=35))


    def backwards(self, orm):
        
        # Deleting field 'UserProfile.level'
        db.delete_column('base_userprofile', 'level')

        # Changing field 'Promocode.promocode_id'
        db.alter_column('base_promocode', 'promocode_id', self.gf('django.db.models.fields.CharField')(max_length=30, unique=True))


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
        'base.comment': {
            'Meta': {'object_name': 'Comment'},
            'comment_id': ('django.db.models.fields.CharField', [], {'default': "'d38c79532b1e39eed0cc46eec3dcd58c'", 'max_length': '32', 'primary_key': 'True'}),
            'message': ('django.db.models.fields.TextField', [], {'max_length': '100'}),
            'owner': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['base.UserProfile']"}),
            'post': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['base.Post']"}),
            'time_created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.date(2012, 1, 5)', 'auto_now_add': 'True', 'blank': 'True'}),
            'time_modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.date(2012, 1, 5)', 'auto_now': 'True', 'blank': 'True'})
        },
        'base.message': {
            'Meta': {'object_name': 'Message'},
            'content': ('django.db.models.fields.TextField', [], {'max_length': '500'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'recipient_id': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'sender_id': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'time': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'})
        },
        'base.photo': {
            'Meta': {'object_name': 'Photo'},
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'photo_id': ('django.db.models.fields.CharField', [], {'default': "'047c7219b20be24cb3446496373b9050'", 'max_length': '32', 'primary_key': 'True'})
        },
        'base.post': {
            'Meta': {'object_name': 'Post'},
            'all_visit': ('django.db.models.fields.PositiveIntegerField', [], {'default': '1'}),
            'message': ('django.db.models.fields.TextField', [], {'max_length': '500'}),
            'owner': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['base.UserProfile']"}),
            'post_id': ('django.db.models.fields.CharField', [], {'default': "'670d8e26c0594f5652fc18a7b0ed97ea'", 'max_length': '32', 'primary_key': 'True'}),
            'time_created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.date(2012, 1, 5)', 'auto_now_add': 'True', 'blank': 'True'}),
            'time_modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.date(2012, 1, 5)', 'auto_now': 'True', 'blank': 'True'}),
            'unique_visit': ('django.db.models.fields.PositiveIntegerField', [], {'default': '1'})
        },
        'base.promocode': {
            'Meta': {'object_name': 'Promocode'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False'}),
            'promocode_id': ('django.db.models.fields.CharField', [], {'default': "'85f7fdcee98eeb11ac1438dc3e59f724'", 'unique': 'True', 'max_length': '35'})
        },
        'base.userprofile': {
            'Meta': {'object_name': 'UserProfile'},
            'accum_cach': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'accum_point': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'cash': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'level': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '1'}),
            'photo': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['base.Photo']", 'unique': 'True', 'null': 'True', 'blank': 'True'}),
            'point': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['auth.User']", 'unique': 'True'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['base']
