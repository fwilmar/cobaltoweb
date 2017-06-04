from rest_framework.routers import DefaultRouter
from sheduler.views import *
from django.conf.urls import url, include
from django.views.generic import TemplateView
from django.template import loader


app_name = 'sheduler'
router = DefaultRouter()
router.register(prefix='doctors', viewset=DoctorViewSet)
router.register(prefix='orders', viewset=OrderViewSet)
router.register(prefix='procedures', viewset=ProcedureViewSet)
router.register(prefix='stations', viewset=LabStationViewSet)

urlpatterns =[
 	url(r'^', include(router.urls)),
 	url(r'^index/$', indexSheduler),
 	url(r'^formorder/$', formOrderView),
 	url(r'^formdoctor/$', formDoctorView),
 	url(r'^editformorder/$', editFormOrderView),
 	url(r'^printorder/$', printOrder),
 	url(r'^printinvoicemontlhy/$', printInvoiceMontlhy),
 	url(r'^dashboard/$', dashboardView),
 ]


