from django.shortcuts import get_object_or_404
from django.views import generic
from .models import Product

class ProductList(generic.ListView):
    model = Product
    context_object_name  = 'products'
    template_name = 'templates/products.html'

class ProductDetail(generic.DetailView):
    model = Product
    context_object_name = 'product'    
    template_name = 'templates/product.html'

    def get_object(self):
        return get_object_or_404(
            Product,
            handle=self.kwargs['handle']
        )
