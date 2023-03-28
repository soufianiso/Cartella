from django.urls import path
from .views import UpdateItem , AddToCart

app_name = "api"

urlpatterns = [
    path("updateitem/<int:pk>/", UpdateItem.as_view(), name="list_product_api"),
    path("addtocart/", AddToCart.as_view(), name="add_to_cart"),
]
