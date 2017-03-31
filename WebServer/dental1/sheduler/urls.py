from rest_framework.routers import DefaultRouter
from sheduler.views import DoctorViewSet,ProcedureViewSet,OrderViewSet
from django.conf.urls import url


app_name = 'sheduler'
router = DefaultRouter()
router.register(prefix='doctors', viewset=DoctorViewSet)
router.register(prefix='orders', viewset=OrderViewSet)
router.register(prefix='procedures', viewset=ProcedureViewSet)


urlpatterns = router.urls



# urlpatterns = [
# 	url(r'^$', views.index_order, name='index_order'),
# 	url(r'^new/order/$', views.add, name='add'),
# ]

