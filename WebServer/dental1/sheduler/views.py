from django.shortcuts import render


# Create your views here.

import sys
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.template import loader
from django.shortcuts import get_object_or_404
from django.views import generic
from .models import Order
from .forms import OrderForm


def add(request):
	if request.method == 'POST':
		form = OrderForm(request.POST)
		if form.is_valid():
			print 'Entro a Save!!!'
			form.save()
			print 'Salio del Save!!!'
		else:
			print 'Invalido!!!'
		return HttpResponseRedirect('/sheduler/')
	else:
		print 'Entro a GET'
		form = OrderForm()
	return render(request, 'sheduler/formOrder.html', {'form':form})


def index_order(request):
	orders=Order.objects.order_by('-date_in')[:100]
	return render(request,'sheduler/indexOrder.html',{'request':request, 'orders':orders})