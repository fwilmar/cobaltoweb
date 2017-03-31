from django.shortcuts import render


# Create your views here.

import sys
import datetime
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.template import loader
from django.shortcuts import get_object_or_404
from django.views import generic
from rest_framework import viewsets
from .models import Order, Doctor, Procedure
from .forms import OrderForm
from .serializers import DoctorSerializer,OrderSerializer,ProcedureSerializer



class DoctorViewSet(viewsets.ModelViewSet):
	queryset = Doctor.objects.all()
	serializer_class = DoctorSerializer


class ProcedureViewSet(viewsets.ModelViewSet):
	queryset = Procedure.objects.all()
	serializer_class = ProcedureSerializer


class OrderViewSet(viewsets.ModelViewSet):
	queryset = Order.objects.all()
	serializer_class = OrderSerializer




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
	now = datetime.datetime.now()
	orders=get_orders_by_month(now)
	return render(request,'sheduler/indexOrder.html',{'request':request, 'orders':orders})

def get_orders_by_month(datefilter):
	print 'Year '+str(datefilter.year)
	print 'Month '+str(datefilter.month)
	orders=Order.objects.filter(date_in__year=datefilter.year, date_in__month=datefilter.month)
	return orders
