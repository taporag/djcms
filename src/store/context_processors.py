from store.models import Product

def all_products(request):    
    products = Product.objects.all()
    return {
        'all_products': products
    }