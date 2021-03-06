from rest_framework import serializers

from .models import Doctor, Procedure, Order, LabStation



class DoctorSerializer(serializers.ModelSerializer):
	#orders = serializers.StringRelatedField(many=True)
	class Meta:
		model = Doctor
		fields = '__all__'

class ProcedureSerializer(serializers.ModelSerializer):
	class Meta:
		model = Procedure
		fields = '__all__'

class LabStationSerializer(serializers.ModelSerializer):
	class Meta:
		model = LabStation
		fields = '__all__'

class OrderSerializer(serializers.ModelSerializer):
	class Meta:
		model = Order
		fields = '__all__'

class OrderSerializerList(serializers.ModelSerializer):
	doctor = serializers.StringRelatedField(many=False)
	procedure = serializers.StringRelatedField(many=False)
	station = serializers.StringRelatedField(many=False)
	date_in = serializers.DateTimeField(format='%m-%d-%Y')
	date_out = serializers.DateTimeField(format='%m-%d-%Y')
	due_date = serializers.DateTimeField(format='%m-%d-%Y')
	class Meta:
		model = Order
		fields = '__all__'


class OrderSerializerPost(serializers.ModelSerializer):
	date_in = serializers.DateTimeField(format='%m-%d-%Y')
	date_out = serializers.DateTimeField(format='%m-%d-%Y')
	class Meta:
		model = Order
		fields = '__all__'