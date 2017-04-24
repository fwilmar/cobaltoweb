from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib.pagesizes import landscape
from reportlab.platypus import Image
from reportlab.lib.units import inch

import csv

import time
from datetime import date



class createPDF():

	def generate_certificate(doctor_name, patient_name, case_number, gap_left, gap_bottom, r ):
		image_width=3.9*inch
		image_height=1.2*inch
		infoLab = 'InfoLab.png'
		r.drawImage(infoLab, 500, 300, width=image_width, height=image_height)
		r.drawCentredString(100,100, "Doctor: "+doctor_name)
		# c.drawCentredString(matrix_components[2][0]+gap_left,matrix_components[2][1]+gap_bottom, "Patient: "+patient_name)
		r.showPage()
		r.save()