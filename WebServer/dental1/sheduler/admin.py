from django.contrib import admin

# Register your models here.
from .models import Order
from .models import Doctor
from .models import Procedure


admin.site.register(Order)
admin.site.register(Doctor)
admin.site.register(Procedure)