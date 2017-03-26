from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib.pagesizes import landscape
from reportlab.platypus import Image
from reportlab.lib.units import inch

import csv

import time
from datetime import date

today = date.today()
print today

#letter size = 8.5inch , 11inch

data_file = 'data.csv'
c = canvas.Canvas("TexasDentalLab-"+str(today)+".pdf", pagesize=letter)


#il=image-left / ib=image-bottom
image_width=3.9*inch
image_height=1.2*inch


w, h = 2, 4;
matrix_components = [[0 for x in range(w)] for y in range(h)] 

#matrix_components contains label coordinates, 
matrix_components[0][0] = 0.2*inch  	#Image distance-left
matrix_components[0][1] = 9*inch 		#Image distance-bottom  
matrix_components[1][0] = 1.6*inch		#Doctor dist-left
matrix_components[1][1] = 8.8*inch		#Doctor dist-bottom
matrix_components[2][0] = 1.6*inch		#Patient dist-left
matrix_components[2][1] = 8.6*inch		#Patient dist-bottom 
matrix_components[3][0] = 3*inch		#CaseNumber dist-left
matrix_components[3][1] = 8.3*inch		#CaseNumber dist-bottom 


# Page
# label 1 | label 2
# label 3 | label 4 
# label 5 | label 6



w, h = 2, 6;
matrix_gap = [[0 for x in range(w)] for y in range(h)]
matrix_gap[0][0] = 0  		#label 1, gap left
matrix_gap[0][1] = 0 		#label 1, gap bottom 
matrix_gap[1][0] = 300		#label 2, gap left
matrix_gap[1][1] = 1		#label 2, gap bottom
matrix_gap[2][0] = 1		#label 3, gap left
matrix_gap[2][1] = -200		#label 3, gap bottom 
matrix_gap[3][0] = 300		#label 4, gap left 
matrix_gap[3][1] = -200		#label 4, gap bottom 
matrix_gap[4][0] = 1		#label 5, gap left 
matrix_gap[4][1] = -400		#label 5, gap bottom 
matrix_gap[5][0] = 300		#label 6, gap left 
matrix_gap[5][1] = -400		#label 6, gap bottom 



def import_data(data_file):
	attendee_data = csv.reader(open(data_file,"rb"))
	num_lab=0
	for row in attendee_data:
		patient_name = row[0]
		doctor_name =  row[1]
		case_number = row[2]
		gap_left=matrix_gap[num_lab][0]
		gap_bottom=matrix_gap[num_lab][1]
		generate_certificate(doctor_name, patient_name, case_number, gap_left, gap_bottom)
		if num_lab == 5:
			num_lab = 0
			c.showPage()
		else:
			num_lab +=1
	c.save()

def generate_certificate(doctor_name, patient_name, case_number, gap_left, gap_bottom):
	infoLab = 'InfoLab.png'
	c.drawImage(infoLab, matrix_components[0][0]+gap_left, matrix_components[0][1]+gap_bottom, width=image_width, height=image_height)
	c.setFont('Helvetica', 11, leading=None)
	c.drawCentredString(matrix_components[1][0]+gap_left,matrix_components[1][1]+gap_bottom, "Doctor: "+doctor_name)
	c.drawCentredString(matrix_components[2][0]+gap_left,matrix_components[2][1]+gap_bottom, "Patient: "+patient_name)
	c.setFont('Helvetica', 8, leading=None)
	c.drawCentredString(matrix_components[3][0]+gap_left,matrix_components[3][1]+gap_bottom,"Case: "+case_number)

import_data(data_file)