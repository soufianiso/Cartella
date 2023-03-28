from django.shortcuts import render
from rest_framework import generics
from rest_framework.decorators import action
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import OrderItemSerializer, AddToCartOrderItemSerializer
from products.models import Product
from cart.models import Order, OrderItem
from django.views.decorators.csrf import csrf_exempt

# Create your views here.


class UpdateItem(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = OrderItemSerializer

    def get_queryset(self):
        order = Order.objects.get(session_id=self.request.session.session_key)
        orderitem = OrderItem.objects.filter(order=order)
        return orderitem

    def perform_update(self, serializer):
        instance = serializer.save()
        if instance.quantity <= 0:
            instance.delete()


class AddToCart(generics.CreateAPIView):
    serializer_class = AddToCartOrderItemSerializer
    queryset = OrderItem.objects.all()

    def perform_create(self, serializer):
        product = serializer.validated_data["product"]
        order, created = Order.objects.get_or_create(
            session_id=self.request.session.session_key
        )
        instance = OrderItem.objects.filter(product=product, order=order).first()
        if not instance:
            serializer.save(order=order)
        instance.quantity += 1
        instance.save()


