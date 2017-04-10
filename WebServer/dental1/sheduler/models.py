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
	doctor = models.ForeignKey(Doctor, on_delete = models.CASCADE, related_name='orders')
	patient = models.CharField(max_length=200)
	procedure = models.ForeignKey(Procedure)
	description = models.CharField(max_length=500)
	date_in = models.DateTimeField('order date in')
	date_out = models.DateTimeField('order date out',null=True)
	cost = models.IntegerField()
	def __unicode__(self):
		return '%d: %s' % (self.case, self.patient)

class Printed(models.Model):
	NEW_STATUS = 1
	IN_PROCESS_STATUS = 2
	ENDED_STATUS = 3
	STATUS_CHOICES = (
		(NEW_STATUS, 'New'),
		(IN_PROCESS_STATUS, 'InProcess'),
		(ENDED_STATUS, 'Ended'),
		)
	date_process_start = models.DateTimeField()
	date_process_end = models.DateTimeField()
	printed_order_status = models.IntegerField()
	status = models.IntegerField(choices=STATUS_CHOICES, default=NEW_STATUS)

class OrderPrinted(models.Model):
	order_id = models.ForeignKey(Order)
	printed_id = models.ForeignKey(Printed)