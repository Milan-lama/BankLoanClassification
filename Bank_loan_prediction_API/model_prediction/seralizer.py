from rest_framework import serializers
from .models import Customer
class CustomerSeralizer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'