from django.urls import path
from .views import addToCart, CartList
app_name = 'cart'
urlpatterns = [
    path('', CartList.as_view(), name='cart_list'),
    path('add/', addToCart, name='add')
]
