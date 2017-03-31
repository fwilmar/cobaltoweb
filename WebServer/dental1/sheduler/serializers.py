from rest_framework import serializers

from .models import Doctor, Procedure, Order



class DoctorSerializer(serializers.ModelSerializer):
	class Meta:
		model = Doctor
		fields = '__all__'

class ProcedureSerializer(serializers.ModelSerializer):
	class Meta:
		model = Procedure
		fields = '__all__'

class OrderSerializer(serializers.ModelSerializer):
	class Meta:
		model = Order
		fields = '__all__'