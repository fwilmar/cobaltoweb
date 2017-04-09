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
from rest_framework.decorators import detail_route, list_route
from rest_framework.response import Response
from rest_framework.renderers import TemplateHTMLRenderer
from django.template import loader
from django.template import RequestContext
import datetime



def indexSheduler(request):
	year = datetime.date.today().year
	month = datetime.date.today().month
	return render(request,'sheduler/indexOrder.html', {'year': year, 'month': month})

def dashboardView(request):
	return render(request,'sheduler/starter.html')


class DoctorViewSet(viewsets.ModelViewSet):
	queryset = Doctor.objects.all()
	serializer_class = DoctorSerializer


class ProcedureViewSet(viewsets.ModelViewSet):
	queryset = Procedure.objects.all()
	serializer_class = ProcedureSerializer


class OrderViewSet(viewsets.ModelViewSet):
	queryset = Order.objects.all()
	serializer_class = OrderSerializer


	@list_route()
	def order_month(self, request):
			year = self.request.query_params.get('year', None)
			month = self.request.query_params.get('month', None)
			if (year != None and month != None ):
				order_month = Order.objects.filter(date_in__year=year, date_in__month=month)
			elif year != None:
				order_month = Order.objects.filter(date_in__year=year)
			else :
				order_month = Order.objects.all()
			page = self.paginate_queryset(order_month)
			if page is not None:
				serializer = self.get_serializer(page, many=True)
				return self.get_paginated_response(serializer.data)
			serializer = self.get_serializer(order_month, many=True)
			data = serializer.data[:]
			return Response(data)


def add(request):
	if request.method == 'POST':
		form = OrderForm(request.POST)
		if form.is_valid():
			print 'Entro a Save!!!'
			form.save()
			print 'Salio del Save!!!'
		else:
			print 'Invalido!!!'
		return HttpResponseRedirect('/sheduler/index')
	else:
		print 'Entro a GET'
		form = OrderForm()
	return render(request, 'sheduler/formOrder.html', {'form':form})
