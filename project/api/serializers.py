from rest_framework import serializers
from cart.models import OrderItem 
class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = ['id','quantity'] 



