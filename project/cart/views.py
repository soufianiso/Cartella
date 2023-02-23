from django.shortcuts import render
from django.views.generic import ListView
from .models import Order
# Create your views here.

class AddToCart(ListView):
    context_object_name= 'orderitem'

    def get_queryset(self):
        order, created = Order.objects.get_or_create(session_id = self.request.session.session_key, compeleted=False )
        order.save()
        item = order.orderitem_set.all()
        return item
         
