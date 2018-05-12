#coding:utf-8
from __future__ import unicode_literals

from django.db import models

class Product(models.Model):

    name = models.CharField(max_length=100,verbose_name="name")
    cost_price = models.FloatField(verbose_name="cost price")
    list_price = models.FloatField(verbose_name="list price")
    description = models.TextField(verbose_name="description")

    class Meta:
        verbose_name="Product"
        verbose_name_plural=verbose_name

