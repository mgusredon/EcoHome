# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'Type'
        db.delete_table(u'core_type')

        # Adding model 'Category'
        db.create_table(u'core_category', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('description', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('set_type', self.gf('django.db.models.fields.CharField')(max_length=10)),
        ))
        db.send_create_signal(u'core', ['Category'])

        # Adding model 'Budget'
        db.create_table(u'core_budget', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('description', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('amount', self.gf('django.db.models.fields.IntegerField')()),
            ('money', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('date', self.gf('django.db.models.fields.DateField')()),
            ('period', self.gf('django.db.models.fields.CharField')(max_length=8, blank=True)),
            ('category', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.Category'])),
            ('created_at', self.gf('django.db.models.fields.DateField')(auto_now_add=True, blank=True)),
            ('updated_at', self.gf('django.db.models.fields.DateField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal(u'core', ['Budget'])

        # Adding model 'Saving'
        db.create_table(u'core_saving', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('description', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('amount', self.gf('django.db.models.fields.IntegerField')()),
            ('money', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('period', self.gf('django.db.models.fields.CharField')(max_length=8, blank=True)),
            ('category', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.Category'], null=True)),
            ('created_at', self.gf('django.db.models.fields.DateField')(auto_now_add=True, blank=True)),
            ('updated_at', self.gf('django.db.models.fields.DateField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal(u'core', ['Saving'])

        # Adding field 'Income.category'
        db.add_column(u'core_income', 'category',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['core.Category']),
                      keep_default=False)

        # Adding field 'Expenses.category'
        db.add_column(u'core_expenses', 'category',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['core.Category']),
                      keep_default=False)

        # Adding field 'Expenses.paid_with'
        db.add_column(u'core_expenses', 'paid_with',
                      self.gf('django.db.models.fields.CharField')(default='income', max_length=10, null=True),
                      keep_default=False)


    def backwards(self, orm):
        # Adding model 'Type'
        db.create_table(u'core_type', (
            ('title', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('description', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('set_type', self.gf('django.db.models.fields.CharField')(max_length=50)),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal(u'core', ['Type'])

        # Deleting model 'Category'
        db.delete_table(u'core_category')

        # Deleting model 'Budget'
        db.delete_table(u'core_budget')

        # Deleting model 'Saving'
        db.delete_table(u'core_saving')

        # Deleting field 'Income.category'
        db.delete_column(u'core_income', 'category_id')

        # Deleting field 'Expenses.category'
        db.delete_column(u'core_expenses', 'category_id')

        # Deleting field 'Expenses.paid_with'
        db.delete_column(u'core_expenses', 'paid_with')


    models = {
        u'core.budget': {
            'Meta': {'object_name': 'Budget'},
            'amount': ('django.db.models.fields.IntegerField', [], {}),
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.Category']"}),
            'created_at': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date': ('django.db.models.fields.DateField', [], {}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'money': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'period': ('django.db.models.fields.CharField', [], {'max_length': '8', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'updated_at': ('django.db.models.fields.DateField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        u'core.category': {
            'Meta': {'object_name': 'Category'},
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'set_type': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'core.expenses': {
            'Meta': {'object_name': 'Expenses'},
            'amount': ('django.db.models.fields.IntegerField', [], {}),
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.Category']"}),
            'created_at': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date': ('django.db.models.fields.DateField', [], {}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'money': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'paid_with': ('django.db.models.fields.CharField', [], {'default': "'income'", 'max_length': '10', 'null': 'True'}),
            'period': ('django.db.models.fields.CharField', [], {'max_length': '8', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'updated_at': ('django.db.models.fields.DateField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        u'core.income': {
            'Meta': {'object_name': 'Income'},
            'amount': ('django.db.models.fields.IntegerField', [], {}),
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.Category']"}),
            'created_at': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date': ('django.db.models.fields.DateField', [], {}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'money': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'period': ('django.db.models.fields.CharField', [], {'max_length': '8', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'updated_at': ('django.db.models.fields.DateField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        u'core.saving': {
            'Meta': {'object_name': 'Saving'},
            'amount': ('django.db.models.fields.IntegerField', [], {}),
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.Category']", 'null': 'True'}),
            'created_at': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'money': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'period': ('django.db.models.fields.CharField', [], {'max_length': '8', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'updated_at': ('django.db.models.fields.DateField', [], {'auto_now': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['core']