from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormView
from .models import Product
from cart.models import Order, OrderItem
from django.urls import reverse_lazy

# Create your views here.


class ListProduct(ListView):
    queryset = Product.objects.all()
    context_object_name = "products"


class DetailProduct(DetailView):
    queryset = Product.objects.all()
    context_object_name = "obj"

    def get_object(self, **kwargs):
        id = self.kwargs.get("id")
        obj = get_object_or_404(Product, id=id)
        return obj
