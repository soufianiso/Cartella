from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormView
from .models import Product
from django.urls import reverse_lazy
# Create your views here.

class ListProduct(ListView):
    queryset = Product.objects.all()
    context_object_name = 'products'
    

class DetailProduct(DetailView):
    model = Product
    context_object_name = 'obj'
   
    def get_object(self, **kwargs):
        id = self.kwargs.get('id')
        obj = get_object_or_404(Product, id=id)
        return obj





