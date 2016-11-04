# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'NouabookItem'
        db.create_table(u'elections_nouabookitem', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=250, null=True, blank=True)),
            ('text', self.gf('django.db.models.fields.TextField')()),
            ('url', self.gf('django.db.models.fields.URLField')(max_length=300, null=True, blank=True)),
            ('urlVideo', self.gf('django.db.models.fields.URLField')(max_length=300, null=True, blank=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('updated', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, null=True, blank=True)),
            ('candidate', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['candideitorg.Candidate'])),
            ('category', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['elections.NouabookCategory'])),
        ))
        db.send_create_signal(u'elections', ['NouabookItem'])

        # Adding model 'Attachment'
        db.create_table(u'elections_attachment', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('modelName', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('file', self.gf('django.db.models.fields.files.FileField')(max_length=100)),
            ('messageId', self.gf('django.db.models.fields.IntegerField')(max_length=10, null=True)),
            ('author_id', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'elections', ['Attachment'])

        # Adding model 'NouabookCategory'
        db.create_table(u'elections_nouabookcategory', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal(u'elections', ['NouabookCategory'])

        # Adding field 'VotaInteligenteMessage.nouabookItem'
        db.add_column(u'elections_votainteligentemessage', 'nouabookItem',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['elections.NouabookItem'], null=True, on_delete=models.SET_NULL, blank=True),
                      keep_default=False)

        # Adding field 'CandidatePerson.canUsername'
        db.add_column(u'elections_candidateperson', 'canUsername',
                      self.gf('django.db.models.fields.related.OneToOneField')(to=orm['auth.User'], unique=True, null=True),
                      keep_default=False)

        # Adding field 'CandidatePerson.ranking'
        db.add_column(u'elections_candidateperson', 'ranking',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting model 'NouabookItem'
        db.delete_table(u'elections_nouabookitem')

        # Deleting model 'Attachment'
        db.delete_table(u'elections_attachment')

        # Deleting model 'NouabookCategory'
        db.delete_table(u'elections_nouabookcategory')

        # Deleting field 'VotaInteligenteMessage.nouabookItem'
        db.delete_column(u'elections_votainteligentemessage', 'nouabookItem_id')

        # Deleting field 'CandidatePerson.canUsername'
        db.delete_column(u'elections_candidateperson', 'canUsername_id')

        # Deleting field 'CandidatePerson.ranking'
        db.delete_column(u'elections_candidateperson', 'ranking')


    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Permission']"}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'candideitorg.answer': {
            'Meta': {'object_name': 'Answer'},
            'caption': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'question': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['candideitorg.Question']"}),
            'remote_id': ('django.db.models.fields.IntegerField', [], {'default': '12'}),
            'resource_uri': ('django.db.models.fields.CharField', [], {'default': "'resource empty'", 'max_length': '255'})
        },
        u'candideitorg.candidate': {
            'Meta': {'object_name': 'Candidate'},
            'answers': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['candideitorg.Answer']", 'null': 'True', 'blank': 'True'}),
            'election': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['candideitorg.Election']"}),
            'has_answered': ('django.db.models.fields.BooleanField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'photo': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'remote_id': ('django.db.models.fields.IntegerField', [], {'default': '12'}),
            'resource_uri': ('django.db.models.fields.CharField', [], {'default': "'resource empty'", 'max_length': '255'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '255'})
        },
        u'candideitorg.category': {
            'Meta': {'object_name': 'Category'},
            'election': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['candideitorg.Election']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'order': ('django.db.models.fields.IntegerField', [], {}),
            'remote_id': ('django.db.models.fields.IntegerField', [], {'default': '12'}),
            'resource_uri': ('django.db.models.fields.CharField', [], {'default': "'resource empty'", 'max_length': '255'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '255'})
        },
        u'candideitorg.election': {
            'Meta': {'object_name': 'Election'},
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'information_source': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'logo': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'remote_id': ('django.db.models.fields.IntegerField', [], {'default': '12'}),
            'resource_uri': ('django.db.models.fields.CharField', [], {'default': "'resource empty'", 'max_length': '255'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '255'}),
            'use_default_media_naranja_option': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        u'candideitorg.question': {
            'Meta': {'object_name': 'Question'},
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['candideitorg.Category']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'question': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'remote_id': ('django.db.models.fields.IntegerField', [], {'default': '12'}),
            'resource_uri': ('django.db.models.fields.CharField', [], {'default': "'resource empty'", 'max_length': '255'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'elections.attachment': {
            'Meta': {'object_name': 'Attachment'},
            'author_id': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'file': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'messageId': ('django.db.models.fields.IntegerField', [], {'max_length': '10', 'null': 'True'}),
            'modelName': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'})
        },
        u'elections.candidateperson': {
            'Meta': {'object_name': 'CandidatePerson'},
            'canUsername': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['auth.User']", 'unique': 'True', 'null': 'True'}),
            'candidate': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "'relation'", 'unique': 'True', 'to': u"orm['candideitorg.Candidate']"}),
            'custom_ribbon': ('django.db.models.fields.CharField', [], {'max_length': '18', 'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'default': "''", 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'person': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "'relation'", 'unique': 'True', 'to': u"orm['popit.Person']"}),
            'portrait_photo': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True', 'blank': 'True'}),
            'ranking': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'reachable': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        u'elections.election': {
            'Meta': {'object_name': 'Election'},
            'can_election': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['candideitorg.Election']", 'unique': 'True', 'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'extra_info_content': ('django.db.models.fields.TextField', [], {'max_length': '3000', 'null': 'True', 'blank': 'True'}),
            'extra_info_title': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'highlighted': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'popit_api_instance': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['popit.ApiInstance']", 'null': 'True', 'blank': 'True'}),
            'searchable': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'slug': ('autoslug.fields.AutoSlugField', [], {'unique': 'True', 'max_length': '50', 'populate_from': "'name'", 'unique_with': '()'}),
            'uses_face_to_face': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'uses_preguntales': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'uses_questionary': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'uses_ranking': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'uses_soul_mate': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'writeitinstance': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['writeit.WriteItInstance']", 'null': 'True', 'blank': 'True'})
        },
        u'elections.nouabookcategory': {
            'Meta': {'object_name': 'NouabookCategory'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'elections.nouabookitem': {
            'Meta': {'object_name': 'NouabookItem'},
            'candidate': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['candideitorg.Candidate']"}),
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['elections.NouabookCategory']"}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'text': ('django.db.models.fields.TextField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'null': 'True', 'blank': 'True'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '300', 'null': 'True', 'blank': 'True'}),
            'urlVideo': ('django.db.models.fields.URLField', [], {'max_length': '300', 'null': 'True', 'blank': 'True'})
        },
        u'elections.votainteligenteanswer': {
            'Meta': {'object_name': 'VotaInteligenteAnswer'},
            'content': ('django.db.models.fields.TextField', [], {}),
            'created': ('django.db.models.fields.DateTimeField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'message': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'answers'", 'to': u"orm['elections.VotaInteligenteMessage']"}),
            'person': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'answers'", 'to': u"orm['popit.Person']"})
        },
        u'elections.votainteligentemessage': {
            'Meta': {'object_name': 'VotaInteligenteMessage', '_ormbases': [u'writeit.Message']},
            'author_ville': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '35'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'fbshared': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'first_moderation': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_video': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'message_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['writeit.Message']", 'unique': 'True', 'primary_key': 'True'}),
            'moderated': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'moderated_at': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'nouabookItem': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['elections.NouabookItem']", 'null': 'True', 'on_delete': 'models.SET_NULL', 'blank': 'True'}),
            'pending_status': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'rejected_status': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        u'popit.apiinstance': {
            'Meta': {'object_name': 'ApiInstance'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'url': ('popit.fields.ApiInstanceURLField', [], {'unique': 'True', 'max_length': '200'})
        },
        u'popit.person': {
            'Meta': {'object_name': 'Person'},
            'api_instance': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['popit.ApiInstance']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'popit_url': ('popit.fields.PopItURLField', [], {'default': "''", 'max_length': '200', 'unique': 'True', 'null': 'True', 'blank': 'True'}),
            'summary': ('django.db.models.fields.TextField', [], {'blank': 'True'})
        },
        u'writeit.message': {
            'Meta': {'object_name': 'Message', '_ormbases': [u'writeit.WriteItDocument']},
            'author_email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'author_name': ('django.db.models.fields.CharField', [], {'max_length': '512'}),
            'content': ('django.db.models.fields.TextField', [], {}),
            'people': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'messages'", 'symmetrical': 'False', 'to': u"orm['popit.Person']"}),
            'slug': ('django.db.models.fields.CharField', [], {'max_length': '512'}),
            'subject': ('django.db.models.fields.CharField', [], {'max_length': '512'}),
            u'writeitdocument_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['writeit.WriteItDocument']", 'unique': 'True', 'primary_key': 'True'}),
            'writeitinstance': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['writeit.WriteItInstance']"})
        },
        u'writeit.writeitapiinstance': {
            'Meta': {'object_name': 'WriteItApiInstance'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'url': ('django.db.models.fields.URLField', [], {'unique': 'True', 'max_length': '200'})
        },
        u'writeit.writeitdocument': {
            'Meta': {'object_name': 'WriteItDocument'},
            'api_instance': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['writeit.WriteItApiInstance']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'remote_id': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'url': ('django.db.models.fields.CharField', [], {'max_length': '256'})
        },
        u'writeit.writeitinstance': {
            'Meta': {'object_name': 'WriteItInstance', '_ormbases': [u'writeit.WriteItDocument']},
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            u'writeitdocument_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['writeit.WriteItDocument']", 'unique': 'True', 'primary_key': 'True'})
        }
    }

    complete_apps = ['elections']