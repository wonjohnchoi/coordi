# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Promocode'
        db.create_table('base_promocode', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('promocode_id', self.gf('django.db.models.fields.CharField')(default='811e941f5f85f850e7d5828d6090e207', unique=True, max_length=30)),
        ))
        db.send_create_signal('base', ['Promocode'])

        # Adding M2M table for field permissions on 'Promocode'
        db.create_table('base_promocode_permissions', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('promocode', models.ForeignKey(orm['base.promocode'], null=False)),
            ('permission', models.ForeignKey(orm['auth.permission'], null=False))
        ))
        db.create_unique('base_promocode_permissions', ['promocode_id', 'permission_id'])

        # Adding model 'Photo'
        db.create_table('base_photo', (
            ('photo_id', self.gf('django.db.models.fields.CharField')(default='90d77239212c8544b4c5dc36541d0898', max_length=32, primary_key=True)),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
        ))
        db.send_create_signal('base', ['Photo'])

        # Adding model 'UserProfile'
        db.create_table('base_userprofile', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['auth.User'], unique=True)),
            ('accum_point', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('accum_cach', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('point', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('cash', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('photo', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['base.Photo'], unique=True, null=True, blank=True)),
        ))
        db.send_create_signal('base', ['UserProfile'])

        # Adding model 'Message'
        db.create_table('base_message', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('content', self.gf('django.db.models.fields.TextField')(max_length=500)),
            ('time', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('sender_id', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('recipient_id', self.gf('django.db.models.fields.CharField')(max_length=30)),
        ))
        db.send_create_signal('base', ['Message'])

        # Adding model 'Post'
        db.create_table('base_post', (
            ('post_id', self.gf('django.db.models.fields.CharField')(default='fc8c1f9eea4fe988cb1412ab0a00a692', max_length=32, primary_key=True)),
            ('owner', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['base.UserProfile'])),
            ('message', self.gf('django.db.models.fields.TextField')(max_length=500)),
            ('time_created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.date(2012, 1, 3), auto_now_add=True, blank=True)),
            ('time_modified', self.gf('django.db.models.fields.DateTimeField')(default=datetime.date(2012, 1, 3), auto_now=True, blank=True)),
            ('unique_visit', self.gf('django.db.models.fields.PositiveIntegerField')(default=1)),
            ('all_visit', self.gf('django.db.models.fields.PositiveIntegerField')(default=1)),
        ))
        db.send_create_signal('base', ['Post'])

        # Adding model 'Comment'
        db.create_table('base_comment', (
            ('comment_id', self.gf('django.db.models.fields.CharField')(default='82464471341d5876e9811d627b92780f', max_length=32, primary_key=True)),
            ('owner', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['base.UserProfile'])),
            ('message', self.gf('django.db.models.fields.TextField')(max_length=100)),
            ('time_created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.date(2012, 1, 3), auto_now_add=True, blank=True)),
            ('time_modified', self.gf('django.db.models.fields.DateTimeField')(default=datetime.date(2012, 1, 3), auto_now=True, blank=True)),
            ('post', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['base.Post'])),
        ))
        db.send_create_signal('base', ['Comment'])


    def backwards(self, orm):
        
        # Deleting model 'Promocode'
        db.delete_table('base_promocode')

        # Removing M2M table for field permissions on 'Promocode'
        db.delete_table('base_promocode_permissions')

        # Deleting model 'Photo'
        db.delete_table('base_photo')

        # Deleting model 'UserProfile'
        db.delete_table('base_userprofile')

        # Deleting model 'Message'
        db.delete_table('base_message')

        # Deleting model 'Post'
        db.delete_table('base_post')

        # Deleting model 'Comment'
        db.delete_table('base_comment')


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
            'comment_id': ('django.db.models.fields.CharField', [], {'default': "'8d3cd3607072766d4c6a14174c9e3e98'", 'max_length': '32', 'primary_key': 'True'}),
            'message': ('django.db.models.fields.TextField', [], {'max_length': '100'}),
            'owner': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['base.UserProfile']"}),
            'post': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['base.Post']"}),
            'time_created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.date(2012, 1, 3)', 'auto_now_add': 'True', 'blank': 'True'}),
            'time_modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.date(2012, 1, 3)', 'auto_now': 'True', 'blank': 'True'})
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
            'photo_id': ('django.db.models.fields.CharField', [], {'default': "'0df0744a12a010c62c075bca755a8bdc'", 'max_length': '32', 'primary_key': 'True'})
        },
        'base.post': {
            'Meta': {'object_name': 'Post'},
            'all_visit': ('django.db.models.fields.PositiveIntegerField', [], {'default': '1'}),
            'message': ('django.db.models.fields.TextField', [], {'max_length': '500'}),
            'owner': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['base.UserProfile']"}),
            'post_id': ('django.db.models.fields.CharField', [], {'default': "'1d4bce9f76cd4d462f2f4d162ae2b4bb'", 'max_length': '32', 'primary_key': 'True'}),
            'time_created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.date(2012, 1, 3)', 'auto_now_add': 'True', 'blank': 'True'}),
            'time_modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.date(2012, 1, 3)', 'auto_now': 'True', 'blank': 'True'}),
            'unique_visit': ('django.db.models.fields.PositiveIntegerField', [], {'default': '1'})
        },
        'base.promocode': {
            'Meta': {'object_name': 'Promocode'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False'}),
            'promocode_id': ('django.db.models.fields.CharField', [], {'default': "'0c73d3140e9be860c723c040e48d62ed'", 'unique': 'True', 'max_length': '30'})
        },
        'base.userprofile': {
            'Meta': {'object_name': 'UserProfile'},
            'accum_cach': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'accum_point': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'cash': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
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
