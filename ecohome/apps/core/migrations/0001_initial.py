# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Income'
        db.create_table(u'core_income', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('description', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('amount', self.gf('django.db.models.fields.IntegerField')()),
            ('money', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('date', self.gf('django.db.models.fields.DateField')()),
            ('period', self.gf('django.db.models.fields.CharField')(max_length=8, blank=True)),
            ('created_at', self.gf('django.db.models.fields.DateField')(auto_now_add=True, blank=True)),
            ('updated_at', self.gf('django.db.models.fields.DateField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal(u'core', ['Income'])

        # Adding model 'Type'
        db.create_table(u'core_type', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('description', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('set_type', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal(u'core', ['Type'])

        # Adding model 'Expenses'
        db.create_table(u'core_expenses', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('description', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('amount', self.gf('django.db.models.fields.IntegerField')()),
            ('money', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('date', self.gf('django.db.models.fields.DateField')()),
            ('period', self.gf('django.db.models.fields.CharField')(max_length=8, blank=True)),
            ('created_at', self.gf('django.db.models.fields.DateField')(auto_now_add=True, blank=True)),
            ('updated_at', self.gf('django.db.models.fields.DateField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal(u'core', ['Expenses'])


    def backwards(self, orm):
        # Deleting model 'Income'
        db.delete_table(u'core_income')

        # Deleting model 'Type'
        db.delete_table(u'core_type')

        # Deleting model 'Expenses'
        db.delete_table(u'core_expenses')


    models = {
        u'core.expenses': {
            'Meta': {'object_name': 'Expenses'},
            'amount': ('django.db.models.fields.IntegerField', [], {}),
            'created_at': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date': ('django.db.models.fields.DateField', [], {}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'money': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'period': ('django.db.models.fields.CharField', [], {'max_length': '8', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'updated_at': ('django.db.models.fields.DateField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        u'core.income': {
            'Meta': {'object_name': 'Income'},
            'amount': ('django.db.models.fields.IntegerField', [], {}),
            'created_at': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date': ('django.db.models.fields.DateField', [], {}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'money': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'period': ('django.db.models.fields.CharField', [], {'max_length': '8', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'updated_at': ('django.db.models.fields.DateField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        u'core.type': {
            'Meta': {'object_name': 'Type'},
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'set_type': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['core']