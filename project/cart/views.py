from django.shortcuts import render
from django.views.generic import ListView, RedirectView
from .models import Order
# Create your views here.

class CartView(ListView):
    context_object_name= 'items'

    def get_queryset(self):
        order, created = Order.objects.get_or_create(session_id = self.request.session.session_key, compeleted=False )
        order.save()
        items = order.orderitem_set.all()
        return items
         
class AddToCart(RedirectView):
    url = '/'
