from django.shortcuts import redirect
from django.db.models import Q
from django.contrib.sessions.models import Session
from django.http import HttpResponse
from django.views.generic import ListView, TemplateView, FormView
from .models import Cart, CartItem
from store.models import Product
from .forms import AddToCartForm
from helpers.helpers import get_user_agent, get_user_ip

class CartList(ListView):
    model = Cart
    template_name= 'templates/cart.html'

def addToCart(request):
    if request.method == 'POST':
        form = AddToCartForm(request.POST)
        if form.is_valid():
            session_id = Session.objects.all()
            user_ip = get_user_ip(request)
            user_agent = get_user_agent(request)
            product_id = request.POST['id']
            quantity = int(request.POST['quantity'])            
            discount = 0.00
            #product = Product.objects.get(Q(id=product_id) || Q(variant__id=product_id))
            #print(product.title)            
            for key, value in session_id:
                print('asd {} => {}'.format(key, value))
            return HttpResponse(f'sucess fully created {session_id}')
    else:
        return redirect('/')