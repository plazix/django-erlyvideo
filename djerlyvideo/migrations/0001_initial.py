# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Server'
        db.create_table('djerlyvideo_server', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('host', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('rtmp_port', self.gf('django.db.models.fields.CharField')(default='1935', max_length=5)),
            ('group', self.gf('django.db.models.fields.CharField')(default=None, max_length=50, null=True, blank=True)),
            ('max_connections', self.gf('django.db.models.fields.IntegerField')(default=None, null=True, blank=True)),
            ('api_port', self.gf('django.db.models.fields.CharField')(default='8082', max_length=5)),
            ('api_user', self.gf('django.db.models.fields.CharField')(default=None, max_length=100, null=True, blank=True)),
            ('api_password', self.gf('django.db.models.fields.CharField')(default=None, max_length=100, null=True, blank=True)),
            ('is_active', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('connections', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('is_broken', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('last_success_ping', self.gf('django.db.models.fields.DateTimeField')()),
        ))
        db.send_create_signal('djerlyvideo', ['Server'])

        # Adding model 'Session'
        db.create_table('djerlyvideo_session', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('server', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['djerlyvideo.Server'])),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(default=None, related_name='erlyvideo_sessions', null=True, blank=True, to=orm['auth.User'])),
            ('type', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('stream', self.gf('django.db.models.fields.CharField')(max_length=50, db_index=True)),
            ('stream_name', self.gf('django.db.models.fields.CharField')(max_length=255, db_index=True)),
            ('start_at', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('finish_at', self.gf('django.db.models.fields.DateTimeField')(default=None, null=True, blank=True)),
        ))
        db.send_create_signal('djerlyvideo', ['Session'])


    def backwards(self, orm):
        
        # Deleting model 'Server'
        db.delete_table('djerlyvideo_server')

        # Deleting model 'Session'
        db.delete_table('djerlyvideo_session')


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
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'djerlyvideo.server': {
            'Meta': {'object_name': 'Server'},
            'api_password': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'api_port': ('django.db.models.fields.CharField', [], {'default': "'8082'", 'max_length': '5'}),
            'api_user': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'connections': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'group': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'host': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_broken': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_success_ping': ('django.db.models.fields.DateTimeField', [], {}),
            'max_connections': ('django.db.models.fields.IntegerField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'rtmp_port': ('django.db.models.fields.CharField', [], {'default': "'1935'", 'max_length': '5'})
        },
        'djerlyvideo.session': {
            'Meta': {'ordering': "('-start_at',)", 'object_name': 'Session'},
            'finish_at': ('django.db.models.fields.DateTimeField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'server': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['djerlyvideo.Server']"}),
            'start_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'stream': ('django.db.models.fields.CharField', [], {'max_length': '50', 'db_index': 'True'}),
            'stream_name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'db_index': 'True'}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'related_name': "'erlyvideo_sessions'", 'null': 'True', 'blank': 'True', 'to': "orm['auth.User']"})
        }
    }

    complete_apps = ['djerlyvideo']
