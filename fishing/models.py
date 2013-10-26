from __future__ import unicode_literals
from django.db import models

class Lake(models.Model):
    name = models.TextField(unique=True)

    def __unicode__(self):
        return self.name


class Type(models.Model):
    name = models.TextField(unique=True)

    def __unicode__(self):
        return self.name


class Rank(models.Model):
    name = models.TextField(unique=True)

    def __unicode__(self):
        return self.name


class Item(models.Model):
    lakes = models.ManyToManyField(Lake, related_name='items')
    value = models.IntegerField(default=0)
    name = models.TextField(unique=True)
    rank = models.ForeignKey(Rank, related_name='ranks', null=True, blank=True)
    type = models.ForeignKey(Type, related_name='types', null=True, blank=True)

    def __unicode__(self):
        return '{} ({}/{}/{})'.format(self.name, self.rank, self.type, self.value)


class Exchange(models.Model):
    output = models.ForeignKey(Item)

    def __unicode__(self):
        return 'Exchange for {}'.format(output.name)


class Component(models.Model):
    exchange = models.ForeignKey(Exchange, related_name='inputs')
    item = models.ForeignKey(Item, related_name='components', null=True, blank=True)
    type = models.ForeignKey(Type, related_name='components', null=True, blank=True)
    quantity = models.IntegerField(default=0)

    def __unicode__(self):
        return '{} of {} for {}'.format(quantity, (item or type).name, exchange.item.name)

    def save(self):
        if not (self.item and not self.type or not self.item and self.type):
            raise ValueError('Either "item" or "type" must be set (not both)')
        return models.Model.save(self)
