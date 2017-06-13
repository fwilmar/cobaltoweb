from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter, inch
from reportlab.lib.pagesizes import landscape
from reportlab.platypus import Image
from reportlab.lib.units import inch

from reportlab.lib.enums import TA_RIGHT
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import Image, Paragraph, SimpleDocTemplate, Table, TableStyle, PageBreak
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors


from django.conf import settings

from django.utils import formats

import csv

import time
from datetime import date



class createPDF():

	def generate_statement(self, orders, response):
		today = date.today()
		c = canvas.Canvas(response, pagesize=letter)
		c = invoice_header(c, orders[1].date_in.strftime('%B - %Y'))

		table_data = []
		table_data.append(['CASE', 'DOCTOR', 'PATIENT', 'PROCEDURE', 'DATE IN', 'DUE DATE', 'DATE OUT', 'COST'])
		t_styles = [
					('ALIGN',(0,0),(-1,-1),'CENTER'),
					('FONT', (0, 0), (-1, 0), 'Helvetica-Bold'),
					('INNERGRID', (0,0), (-1,-1), 0.25, colors.black),
					('BOX', (0,0), (-1,-1), 0.50, colors.black),
					]
		lin = 0
		tot = 0
		page = 1
		for i, order in enumerate(orders):
			# Add a row to the table
			due_date_aux = ''
			date_out_aux = ''
			date_in_aux = ''
			if(order.date_out is not None):
				date_out_aux = order.date_out.strftime('%m/%d/%Y')
			if(order.due_date is not None):
				due_date_aux = order.due_date.strftime('%m/%d/%Y')
			if(order.date_in is not None):
				date_in_aux = order.date_in.strftime('%m/%d/%Y')
			table_data.append([order.case,
								order.doctor.name,
								order.patient,
								order.procedure.name,
								date_in_aux,
								due_date_aux,
								date_out_aux,
								order.cost])
			lin += 1
			tot += order.cost
			if lin > 34:
				c = invoice_header(c, orders[1].date_in.strftime('%B - %Y'))
				order_table = Table(table_data, splitByRow=1)
				order_table.setStyle(TableStyle(t_styles))
				order_table.wrapOn(c, 0, 0)
				order_table.drawOn(c, 40, 70)
				c.setFont('Helvetica', 8)
				c.drawString(500,40,'Page  '+str(page))
				c.showPage()
				lin = 0
				page += 1
				table_data = []
				table_data.append(['CASE', 'DOCTOR', 'PATIENT', 'PROCEDURE', 'DATE IN', 'DUE DATE', 'DATE OUT', 'COST'])
		if lin != 34:
			c = invoice_header(c, orders[1].date_in.strftime('%B - %Y'))
			order_table = Table(table_data, splitByRow=1)
			order_table.setStyle(TableStyle(t_styles))
			order_table.wrapOn(c, 0, 0)
			order_table.drawOn(c, 40, 64+(650-(lin * (650/34))))
			# print "contador "+str(lin)
			# print "contador 1 "+str(lin * (650/34))
			# print "contador 2 "+str(64+(650-(lin * (650/34))))

		c.setFont('Helvetica-Bold', 18)
		c.drawString(40,40,'TOTAL:  '+str(tot))
		c.setFont('Helvetica', 8)
		c.drawString(500,40,'Page  '+str(page))
		c.drawString(500,30,'LAST PAGE')
		c.save()



	def generate_order(self, order, response):
		today = date.today()
		pdfFile = canvas.Canvas(response, pagesize=letter)
		image_width_logo=0.8*inch
		image_height_logo=0.4*inch
		logo1 = 'sheduler/static/img/Logo1-country.jpeg'
		pdfFile.drawImage(logo1, 270, 720, width=image_width_logo, height=image_height_logo)

		pdfFile.setLineWidth(.8)
		pdfFile.setFont('Helvetica-Bold', 18)
		pdfFile.drawString(50,770,'Texas Dental Services Lab')


		pdfFile.roundRect(20, 650, 320, 110, 4, stroke=1, fill=0)
		pdfFile.setFont('Helvetica-Bold', 14)
		pdfFile.drawString(115,740,'CASE: ')
		pdfFile.setFont('Helvetica', 14)
		pdfFile.drawString(190,740,str(order.case))


		pdfFile.setLineWidth(.3)
		pdfFile.setFont('Helvetica-Bold', 11)
		pdfFile.drawString(30,720,'DOCTOR: ')
		pdfFile.drawString(30,700,'PATIENT:')
		pdfFile.drawString(30,680,'DATE IN:')
		pdfFile.drawString(200,680,'DUE DATE:')
		pdfFile.drawString(30,660,'PROCEDURE:')

		pdfFile.setFont('Helvetica', 11)

		pdfFile.drawString(120,720,str(order.doctor))
		pdfFile.line(118,717,250,717)


		pdfFile.drawString(120,700,str(order.patient))
		pdfFile.line(118,697,250,697)


		pdfFile.drawString(120,680,str(formats.date_format(order.date_in, 'm-d-Y')))
		pdfFile.line(118,677,190,677)



		if(order.due_date != None):
			pdfFile.drawString(275,680,str(formats.date_format(order.due_date, 'm-d-Y')))
		pdfFile.line(271,677,335,677)


		pdfFile.drawString(125,660,str(order.procedure))
		pdfFile.line(118,657,250,657)

	# INSTRUCCIONES
		pdfFile.setFont('Helvetica-Bold', 14)
		pdfFile.drawString(100,620,'LAB INSTRUCTIONS')
		pdfFile.setFont('Helvetica', 10)
		pdfFile.drawString(40,600,str(order.description))
		pdfFile.roundRect(20, 580, 320, 55, 4, stroke=1, fill=0)


		dentalImage1 = 'sheduler/static/img/dentalImage1.png'
		pdfFile.drawImage(dentalImage1, 15, 380, width=4.5*inch, height=2.1*inch)
		pdfFile.roundRect(20, 370, 320, 190, 4, stroke=1, fill=0)

	# LABEL

		image_width=3.5*inch
		image_height=1.1*inch
		infoLab = 'sheduler/static/img/PrintLabelTDSLab.png'
		pdfFile.drawImage(infoLab, 40, 160, width=image_width, height=image_height)

		pdfFile.line(40,160,300,160)

		pdfFile.setFont('Helvetica-Bold', 11)
		pdfFile.drawString(100,135,'Doctor: ')
		pdfFile.drawString(100,115,'Patient:')

		pdfFile.setFont('Helvetica', 10)
		pdfFile.drawString(145,135,str(order.doctor))
		pdfFile.drawString(145,115,str(order.patient))

		pdfFile.setFont('Helvetica', 6)
		pdfFile.drawString(240,95,'Case: ')
		pdfFile.drawString(255,95,str(order.case))

	# SEGUNDA COLUMNA

		x=730
		pdfFile.drawImage(logo1, 400, x-15, width=image_width_logo, height=image_height_logo)

		pdfFile.setLineWidth(.8)
		pdfFile.setFont('Helvetica-Bold', 14)
		pdfFile.drawString(470,x,'Invoice')


		pdfFile.setLineWidth(.3)
		pdfFile.setFont('Helvetica-Bold', 11)
		pdfFile.drawString(420,x-55,'Case: ')
		pdfFile.drawString(420,x-70,'Doctor: ')
		pdfFile.drawString(420,x-85,'Patient:')
		pdfFile.drawString(420,x-100,'Date In:')
		pdfFile.drawString(420,x-115,'Due Date:')
		pdfFile.drawString(420,x-130,'Procedure:')
		pdfFile.drawString(420,x-145,'Cost:')



		pdfFile.setFont('Helvetica', 10)
		pdfFile.drawString(465,x-55,str(order.case))
		pdfFile.drawString(465,x-70,str(order.doctor))
		pdfFile.drawString(465,x-85,str(order.patient))
		pdfFile.drawString(465,x-100,str(formats.date_format(order.date_in, 'm-d-Y')))
		if(order.due_date != None):
			pdfFile.drawString(480,x-115,str(formats.date_format(order.due_date, 'm-d-Y')))
		pdfFile.drawString(480,x-130,str(order.procedure))
		pdfFile.drawString(465,x-145,'$ '+str(order.cost))
		pdfFile.roundRect(410, x-155, 145, 125, 4, stroke=1, fill=0)


		pdfFile.setFont('Helvetica-Bold', 12)
		pdfFile.drawString(420,x-210,'Delivery:')
		pdfFile.drawString(420,x-235,'Date Out:')
		pdfFile.line(480,x-210,535,x-210)
		pdfFile.setFont('Helvetica', 10)
		if(order.date_out != None):
			pdfFile.drawString(480,x-235,str(formats.date_format(order.date_out, 'm-d-Y')))
		pdfFile.line(480,x-237,535,x-237)
		pdfFile.roundRect(410, x-245, 145, 60, 4, stroke=1, fill=0)



		pdfFile.showPage()
		pdfFile.save()

def invoice_header(c, month):
	today = date.today()

	c.setFont('Helvetica-Bold', 16)
	c.drawString(50,755,'German Dental Lab')
	c.setFont('Helvetica-Bold', 14)
	c.drawString(50,735,'Ship to: ')
	c.setFont('Helvetica', 14)
	c.drawString(110,735,'Texas Dental Services Lab')
	c.setFont('Helvetica', 14)
	c.drawString(370,755,'Statement - '+month)
	c.setFont('Helvetica', 8)
	c.drawString(450,735,'Printed: '+today.strftime('%m/%d/%Y'))


	return c