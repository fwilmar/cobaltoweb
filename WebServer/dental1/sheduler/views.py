from django.shortcuts import render


# Create your views here.

import sys
from datetime import datetime
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.template import loader
from django.shortcuts import get_object_or_404
from django.views import generic

from rest_framework import viewsets, status
from rest_framework import generics
from rest_framework.decorators import detail_route, list_route,api_view
from rest_framework.response import Response
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.views import APIView

from .models import Order, Doctor, Procedure, LabStation
from .forms import OrderForm
from .serializers import DoctorSerializer,OrderSerializer,ProcedureSerializer,OrderSerializerPost, LabStationSerializer

from django.template import loader
from django.template import RequestContext




def indexSheduler(request):
	return render(request,'sheduler/indexOrder.html')

def dashboardView(request):
	return render(request,'sheduler/starter.html')

def newOrderView(request):
	return render(request,'sheduler/newOrder.html')


class DoctorViewSet(viewsets.ModelViewSet):
	queryset = Doctor.objects.all()
	serializer_class = DoctorSerializer


class ProcedureViewSet(viewsets.ModelViewSet):
	queryset = Procedure.objects.all()
	serializer_class = ProcedureSerializer

class LabStationViewSet(viewsets.ModelViewSet):
	queryset = LabStation.objects.all()
	serializer_class = LabStationSerializer


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
				order_month = Order.objects.filter(date_in__year=datetime.now().year, date_in__month=datetime.now().month)
			page = self.paginate_queryset(order_month)
			if page is not None:
				serializer = self.get_serializer(page, many=True)
				return self.get_paginated_response(serializer.data)
			serializer = self.get_serializer(order_month, many=True)
			data = serializer.data[:]
			return Response(data)


@api_view(['GET', 'POST', 'DELETE'])
def createOrder(request):
	serializer = OrderSerializerPost(data=request.data)
	if serializer.is_valid():
		serializer.save()
		return Response(serializer.data, status=status.HTTP_201_CREATED)
	return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST', 'DELETE'])
def add(request):
	print 'Entro a evaluar!!!'
	if request.method == 'POST':
		serializer = OrderSerializer(data=request.data)
		print request.data
		if serializer.is_valid():
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
