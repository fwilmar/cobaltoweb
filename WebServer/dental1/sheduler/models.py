from __future__ import unicode_literals

from django.db import models

# Create your models here.
from django.forms import ModelForm


class Doctor(models.Model):
	name = models.CharField(max_length=200)
	def __str__(self):
		return self.name

class Procedure(models.Model):
	name = models.CharField(max_length=200)
	def __str__(self):
		return self.name

class Order(models.Model):
	case = models.IntegerField()
	doctor = models.ForeignKey(Doctor, on_delete = models.DO_NOTHING)
	patient = models.CharField(max_length=200)
	procedure = models.ForeignKey(Procedure)
	description = models.CharField(max_length=500)
	date_in = models.DateTimeField('order date in')
	date_out = models.DateTimeField('order date out')