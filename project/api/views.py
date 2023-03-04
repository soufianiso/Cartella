from django.shortcuts import render
from rest_framework import generics
from rest_framework.decorators import action
from .serializers import OrderItemSerializer
from products.models import Product
from cart.models import Order, OrderItem
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

class UpdateItem(generics.RetrieveUpdateDestroyAPIView):
        serializer_class = OrderItemSerializer
        lookup_field= 'id'

        def get_queryset(self):
            order = Order.objects.get(session_id = self.request.session.session_key)
            orderitem = OrderItem.objects.filter(order = order)
            return orderitem

        def perform_update(self, serializer):
            instance = serializer.save()
            print(instance)
            if instance.quantity <= 0:
                instance.delete() 



        

     


















"""class ListProductApi(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ListProductSerializer

class DetailProductApi(generics.ListAPIView):
    serializer_class = DetailProductSerializer

    def get_querset(self, *args, **kwargs):
        instance = Product.objects.get(id = self.kwargs.get('pk'))
        return instance """
