from django.urls import path
from .views import ProductList, ProductDetail
app_name = 'store'
urlpatterns = [
    path('', ProductList.as_view(), name='all'),
    path('<slug:handle>', ProductDetail.as_view(), name='detail'),
]

