from django.shortcuts import render, redirect
from django.views.generic import ListView, RedirectView, DetailView, View
from .models import Order, OrderItem
from products.models import Product
# Create your views here.
class CartView(ListView):
    context_object_name= 'items'

    def get_queryset(self):
        order, created = Order.objects.get_or_create(session_id = self.request.session.session_key, compeleted=False )
        order.save()
        items = order.orderitem_set.all()
        return items
         

class AddToCart(View):
    def get(self, request, *args, **kwargs):
        order, created  = Order.objects.get_or_create(session_id = self.request.session.session_key, compeleted = False)
        product = Product.objects.get(id = self.kwargs.get('pk'))
        orderitem, created = OrderItem.objects.get_or_create(product=product, order=order)
        if not created:
            orderitem.quantity += 1 
            orderitem.save()
        return redirect ('/cart')
