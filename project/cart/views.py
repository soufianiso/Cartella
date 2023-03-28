from django.shortcuts import render, redirect
from django.views.generic import ListView, RedirectView, DetailView, View
from .models import Order, OrderItem
from products.models import Product


# Create your views here.
class CartView(ListView):
    context_object_name = "items"

    def get_queryset(self):
        order, created= Order.objects.get_or_create(
            session_id=self.request.session.session_key, compeleted=False
        )
        items = order.orderitem_set.all()
        return items

    def get_context_data(self):
        context = super().get_context_data()
        context["order"] = Order.objects.get(
            session_id=self.request.session.session_key
        )
        return context
