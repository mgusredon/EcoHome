from django.db import models
from django.utils.translation import ugettext as _


SET_TYPE = (
        ('income', _('Income')),
        ('expenses', _('Expenses')),
        ('saving', _('Saving')),
    )

SET_PAID = (
        ('income', _('Income')),
        ('saving', _('Saving')),
        ('card', _('Card')),
    )

class Category(models.Model):
    title = models.CharField(max_length=50, verbose_name=_('Title'))
    description = models.TextField(blank=True, verbose_name=_('Description'))
    set_type = models.CharField(max_length=10, choices=SET_TYPE, verbose_name=_('Set type'))

    class Meta:
        verbose_name = _('Category')
        verbose_name_plural = _('Categories')

    def __unicode__(self):
        return self.title


class Income(models.Model):
    title = models.CharField(max_length=50, null=False, verbose_name=_('Title'))
    description = models.TextField(blank=True, verbose_name=_('Description'))
    amount = models.IntegerField(blank=False, verbose_name=_('Amount'))
    money = models.CharField(max_length=10, verbose_name=_('Money'))
    date = models.DateField(null=False, verbose_name=_('Date'))
    period = models.CharField(max_length=8, blank=True, verbose_name=_('Period'))
    category = models.ForeignKey(Category, null=False, verbose_name=_('Category'))

    created_at = models.DateField(auto_now_add=True, verbose_name=_('Created at'))
    updated_at = models.DateField(auto_now=True, verbose_name=_('Updated at'))

    class Meta:
        verbose_name = _('Income')
        verbose_name_plural = _('Incomes')

    def __unicode__(self):
        return self.title


class Expenses(models.Model):
    title = models.CharField(max_length=50, null=False, verbose_name=_('Title'))
    description = models.TextField(blank=True, verbose_name=_('Description'))
    amount = models.IntegerField(blank=False, verbose_name=_('Amount'))
    money = models.CharField(max_length=10, verbose_name=_('Money'))
    date = models.DateField(null=False, verbose_name=_('Date'))
    period = models.CharField(max_length=8, blank=True, verbose_name=_('Period'))
    category = models.ForeignKey(Category, null=False, verbose_name=_('Category'))
    paid_with = models.CharField(max_length=10, null=True, default='income', choices=SET_PAID, verbose_name=_('Paid with'))
    paid_category = models.CharField(max_length=10, null=True, verbose_name=_('Paid Category')) # This field is ativity then paid_with choose 

    created_at = models.DateField(auto_now_add=True, verbose_name=_('Created at'))
    updated_at = models.DateField(auto_now=True, verbose_name=_('Updated at'))

    class Meta:
        verbose_name = _('Expense')
        verbose_name_plural = _('Expenses')

    def __unicode__(self):
        return self.title


class Budget(models.Model):
    title = models.CharField(max_length=50, verbose_name=_('Title'))
    description = models.TextField(blank=True, verbose_name=_('Description'))
    amount = models.IntegerField(blank=False, verbose_name=_('Amount'))
    money = models.CharField(max_length=10, verbose_name=_('Money'))
    date = models.DateField(null=False, verbose_name=_('Date'))
    period = models.CharField(max_length=8, blank=True, verbose_name=_('Period'))
    category = models.ForeignKey(Category, null=False, verbose_name=_('Category'))

    created_at = models.DateField(auto_now_add=True, verbose_name=_('Created at'))
    updated_at = models.DateField(auto_now=True, verbose_name=_('Updated at'))

    class Meta:
        verbose_name = _('Budget')
        verbose_name_plural = _('Budgetes')

    def __unicode__(self):
        return self.title


class Saving(models.Model):
    title = models.CharField(max_length=50, verbose_name=_('Title'))
    description = models.TextField(blank=True, verbose_name=_('Description'))
    amount = models.IntegerField(blank=False, verbose_name=_('Amount'))
    money = models.CharField(max_length=10, verbose_name=_('Money'))
    period = models.CharField(max_length=8, blank=True, verbose_name=_('Period'))
    category = models.ForeignKey(Category, null=True, verbose_name=_('Category'))
    
    created_at = models.DateField(auto_now_add=True, verbose_name=_('Created at'))
    updated_at = models.DateField(auto_now=True, verbose_name=_('Updated at'))

    class Meta:
        verbose_name = _('Saving')
        verbose_name_plural = _('Savings')

    def __unicode__(self):
        return self.title
