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
		order_month = Order.objects.filter(date_in__year=year, date_in__month=month)
		page = self.paginate_queryset(order_month)
		if page is not None:
			serializer = self.get_serializer(page, many=True)
			return self.get_paginated_response(serializer.data)
		serializer = self.get_serializer(order_month, many=True)
		return Response(serializer.data)