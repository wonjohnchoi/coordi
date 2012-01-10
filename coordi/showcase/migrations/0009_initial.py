# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Showcase'
        db.create_table('showcase_showcase', (
            ('showcase_id', self.gf('django.db.models.fields.CharField')(default='dce6c57225e55f98dccf8c5a78ccc9ff', max_length=32, primary_key=True)),
            ('is_votable', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('is_editable', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('is_viewable', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('is_closed', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('episode_id', self.gf('django.db.models.fields.PositiveSmallIntegerField')(unique=True)),
        ))
        db.send_create_signal('showcase', ['Showcase'])

        # Adding model 'Theme'
        db.create_table('showcase_theme', (
            ('theme_id', self.gf('django.db.models.fields.CharField')(default='887ac622032e8032bf2cf71ed408cd52', max_length=32, primary_key=True)),
            ('showcase', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['showcase.Showcase'])),
            ('keyword', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('subject', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('theme_pos', self.gf('django.db.models.fields.PositiveSmallIntegerField')()),
        ))
        db.send_create_signal('showcase', ['Theme'])

        # Adding model 'Album'
        db.create_table('showcase_album', (
            ('album_id', self.gf('django.db.models.fields.CharField')(default='7f6cdc285c539a89f06d27fff46495d1', max_length=32, primary_key=True)),
            ('theme', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['showcase.Theme'])),
            ('coordi', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('title', self.gf('django.db.models.fields.CharField')(default=u'Untitled', max_length=50, null=True, blank=True)),
        ))
        db.send_create_signal('showcase', ['Album'])

        # Adding model 'Unlock'
        db.create_table('showcase_unlock', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('theme', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['showcase.Theme'])),
            ('voter', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['auth.User'], unique=True)),
        ))
        db.send_create_signal('showcase', ['Unlock'])

        # Adding model 'Vote'
        db.create_table('showcase_vote', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('album', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['showcase.Album'])),
            ('voter', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
        ))
        db.send_create_signal('showcase', ['Vote'])

        # Adding model 'Entry'
        db.create_table('showcase_entry', (
            ('entry_id', self.gf('django.db.models.fields.CharField')(default='379391bae2d07c6b1418f334d78302d6', max_length=32, primary_key=True)),
            ('album', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['showcase.Album'])),
            ('entry_pos', self.gf('django.db.models.fields.PositiveSmallIntegerField')()),
            ('text', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('photo', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['base.Photo'], unique=True)),
        ))
        db.send_create_signal('showcase', ['Entry'])


    def backwards(self, orm):
        
        # Deleting model 'Showcase'
        db.delete_table('showcase_showcase')

        # Deleting model 'Theme'
        db.delete_table('showcase_theme')

        # Deleting model 'Album'
        db.delete_table('showcase_album')

        # Deleting model 'Unlock'
        db.delete_table('showcase_unlock')

        # Deleting model 'Vote'
        db.delete_table('showcase_vote')

        # Deleting model 'Entry'
        db.delete_table('showcase_entry')


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
            'photo_id': ('django.db.models.fields.CharField', [], {'default': "'9bca5870ea0792315d3fbcf4ac3b9243'", 'max_length': '32', 'primary_key': 'True'})
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
            'album_id': ('django.db.models.fields.CharField', [], {'default': "'266998fb30e21bce228ee63698569b53'", 'max_length': '32', 'primary_key': 'True'}),
            'coordi': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"}),
            'theme': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['showcase.Theme']"}),
            'title': ('django.db.models.fields.CharField', [], {'default': "u'Untitled'", 'max_length': '50', 'null': 'True', 'blank': 'True'})
        },
        'showcase.entry': {
            'Meta': {'object_name': 'Entry'},
            'album': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['showcase.Album']"}),
            'entry_id': ('django.db.models.fields.CharField', [], {'default': "'38004b7fb3a3e8ce4130473dc671eccb'", 'max_length': '32', 'primary_key': 'True'}),
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
            'showcase_id': ('django.db.models.fields.CharField', [], {'default': "'e45fb1e28e838903a67379401d4b9485'", 'max_length': '32', 'primary_key': 'True'})
        },
        'showcase.theme': {
            'Meta': {'object_name': 'Theme'},
            'keyword': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'showcase': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['showcase.Showcase']"}),
            'subject': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'theme_id': ('django.db.models.fields.CharField', [], {'default': "'8af0b1dfc85d7117822dfee49207f772'", 'max_length': '32', 'primary_key': 'True'}),
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
