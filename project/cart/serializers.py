from rest_framework import serializers
from .models import OrderItem

class ItemsSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = '__all__'

