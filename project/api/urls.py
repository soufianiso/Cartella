from django.urls import path 
from .views import UpdateItem
app_name = 'api' 

urlpatterns = [
    
        path('updateitem/<int:id>/', UpdateItem.as_view(), name='list_product_api'),
     ]

