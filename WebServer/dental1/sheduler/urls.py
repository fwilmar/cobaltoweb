from rest_framework.routers import DefaultRouter
from sheduler.views import DoctorViewSet,ProcedureViewSet,OrderViewSet,indexSheduler, add,dashboardView, newOrderView,createOrder,LabStationViewSet
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
 	url(r'^neworder/$', newOrderView),
 	url(r'^new/order/$', add, name='add'),
 	url(r'^createorder/$', createOrder),
 	url(r'^dashboard/$', dashboardView),
 ]


