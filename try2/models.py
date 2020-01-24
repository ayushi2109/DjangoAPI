# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


# Create your models here.

class Fields(models.Model):

	operand1 = models.IntegerField(max_length=5)
	operand2 = models.IntegerField(max_length=5)
	operator = models.CharField(max_length=5)
	total = models.IntegerField(max_length=5)
