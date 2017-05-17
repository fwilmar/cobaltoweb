from django.shortcuts import render


# Create your views here.

import sys
from datetime import datetime
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.template import loader
from django.shortcuts import get_object_or_404
from django.views import generic
from django.utils import formats

from rest_framework import viewsets, status
from rest_framework import generics
from rest_framework.decorators import detail_route, list_route,api_view
from rest_framework.response import Response
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.views import APIView

from .models import Order, Doctor, Procedure, LabStation
from .forms import OrderForm
from .serializers import DoctorSerializer,OrderSerializer,OrderSerializerList,ProcedureSerializer,OrderSerializerPost, LabStationSerializer

from django.template import loader
from django.template import RequestContext

import cStringIO

from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib.pagesizes import landscape
from reportlab.platypus import Image
from reportlab.lib.units import inch
from wsgiref.util import FileWrapper
import csv

import time
from datetime import date

from printer import createPDF

def indexSheduler(request):
	return render(request,'sheduler/indexOrder.html')

def dashboardView(request):
	return render(request,'sheduler/starter.html')

def formOrderView(request):
	return render(request,'sheduler/formOrder.html')

def formDoctorView(request):
	return render(request,'sheduler/formDoctor.html')


def editFormOrderView(request):
	return render(request,'sheduler/editFormOrder.html')


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
				serializer = OrderSerializerList(page, many=True)
				return self.get_paginated_response(serializer.data)
			serializer = OrderSerializerList(order_month, many=True)
			data = serializer.data[:]
			return Response(data)

@api_view(['GET', 'POST', 'DELETE'])
def printOrder(request):
	id_order = request.query_params.get('fonum', None)
	if id_order != None:
		order = Order.objects.get(id=id_order)

	today = date.today()
	# pdf_file = open("TexasDentalLab-"+str(today)+".pdf", 'rb')
	response = HttpResponse(content_type='application/pdf')
	response['Content-Disposition'] = 'attachment; filename="%s"' % "TexasDentalLab"+str(order.case)+"-"+str(today)+".pdf"
	p = canvas.Canvas(response)
	c = canvas.Canvas("TexasDentalLab"+str(order.case)+"-"+str(today)+".pdf", pagesize=letter)
	generate_certificate(order, p)
	# generate_certificate(str(id_order),"345","567",300, 0 , c)
	return response


def generate_certificate(order ,canvas):

	image_width_logo=0.8*inch
	image_height_logo=0.4*inch
	logo1 = 'sheduler/static/img/Logo1-country.jpeg'
	canvas.drawImage(logo1, 270, 720, width=image_width_logo, height=image_height_logo)

	canvas.setLineWidth(.8)
	canvas.setFont('Helvetica-Bold', 18)
	canvas.drawString(50,770,'Texas Dental Services Lab')


	canvas.roundRect(20, 650, 320, 110, 4, stroke=1, fill=0)
	canvas.setFont('Helvetica-Bold', 14)
	canvas.drawString(115,740,'CASE: ')
	canvas.setFont('Helvetica', 14)
	canvas.drawString(190,740,str(order.case))


	canvas.setLineWidth(.3)
	canvas.setFont('Helvetica-Bold', 11)
	canvas.drawString(30,720,'DOCTOR: ')
	canvas.drawString(30,700,'PATIENT:')
	canvas.drawString(30,680,'DATE IN:')
	canvas.drawString(200,680,'DUE DATE:')
	canvas.drawString(30,660,'PROCEDURE:')

	canvas.setFont('Helvetica', 11)

	canvas.drawString(120,720,str(order.doctor))
	canvas.line(118,717,250,717)


	canvas.drawString(120,700,str(order.patient))
	canvas.line(118,697,250,697)


	canvas.drawString(120,680,str(formats.date_format(order.date_in, 'm-d-Y')))
	canvas.line(118,677,190,677)



	if(order.due_date != None):
		canvas.drawString(275,680,str(formats.date_format(order.due_date, 'm-d-Y')))
	canvas.line(271,677,335,677)


	canvas.drawString(125,660,str(order.procedure))
	canvas.line(118,657,250,657)


# INSTRUCCIONES
	canvas.setFont('Helvetica-Bold', 14)
	canvas.drawString(100,620,'LAB INSTRUCTIONS')
	canvas.setFont('Helvetica', 10)
	canvas.drawString(40,600,str(order.description))
	canvas.roundRect(20, 580, 320, 55, 4, stroke=1, fill=0)


	dentalImage1 = 'sheduler/static/img/dentalImage1.png'
	canvas.drawImage(dentalImage1, 15, 380, width=4.5*inch, height=2.1*inch)
	canvas.roundRect(20, 370, 320, 190, 4, stroke=1, fill=0)

# LABEL

	image_width=3.5*inch
	image_height=1.1*inch
	infoLab = 'sheduler/static/img/PrintLabelTDSLab.png'
	canvas.drawImage(infoLab, 40, 160, width=image_width, height=image_height)

	canvas.line(40,160,300,160)

	canvas.setFont('Helvetica-Bold', 11)
	canvas.drawString(100,135,'Doctor: ')
	canvas.drawString(100,115,'Patient:')

	canvas.setFont('Helvetica', 10)
	canvas.drawString(145,135,str(order.doctor))
	canvas.drawString(145,115,str(order.patient))

	canvas.setFont('Helvetica', 6)
	canvas.drawString(240,95,'Case: ')
	canvas.drawString(255,95,str(order.case))


# SEGUNDA COLUMNA

	x=730
	canvas.drawImage(logo1, 400, x-15, width=image_width_logo, height=image_height_logo)

	canvas.setLineWidth(.8)
	canvas.setFont('Helvetica-Bold', 14)
	canvas.drawString(470,x,'Invoice')


	canvas.setLineWidth(.3)
	canvas.setFont('Helvetica-Bold', 11)
	canvas.drawString(420,x-55,'Case: ')
	canvas.drawString(420,x-70,'Doctor: ')
	canvas.drawString(420,x-85,'Patient:')
	canvas.drawString(420,x-100,'Date In:')
	canvas.drawString(420,x-115,'Due Date:')
	canvas.drawString(420,x-130,'Procedure:')
	canvas.drawString(420,x-145,'Cost:')



	canvas.setFont('Helvetica', 10)
	canvas.drawString(465,x-55,str(order.case))
	canvas.drawString(465,x-70,str(order.doctor))
	canvas.drawString(465,x-85,str(order.patient))
	canvas.drawString(465,x-100,str(formats.date_format(order.date_in, 'm-d-Y')))
	if(order.due_date != None):
		canvas.drawString(480,x-115,str(formats.date_format(order.due_date, 'm-d-Y')))
	canvas.drawString(480,x-130,str(order.procedure))
	canvas.drawString(465,x-145,'$ '+str(order.cost))
	canvas.roundRect(410, x-155, 145, 125, 4, stroke=1, fill=0)


	canvas.setFont('Helvetica-Bold', 12)
	canvas.drawString(420,x-210,'Delivery:')
	canvas.drawString(420,x-235,'Date Out:')
	canvas.line(480,x-210,535,x-210)
	canvas.setFont('Helvetica', 10)
	if(order.date_out != None):
		canvas.drawString(480,x-235,str(formats.date_format(order.date_out, 'm-d-Y')))
	canvas.line(480,x-237,535,x-237)
	canvas.roundRect(410, x-245, 145, 60, 4, stroke=1, fill=0)



	canvas.showPage()
	canvas.save()
