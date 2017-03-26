from django import forms
from .models import Doctor
from .models import Procedure
from .models import Order

class OrderForm(forms.ModelForm):
	class Meta:
		model = Order
		fields = '__all__'
	