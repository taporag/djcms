from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Page
from store.models import Product

class HomeView(generic.TemplateView):
    template_name = 'templates/index.html'
    
    def get_context_data(self, *args, **kwargs):
        context = super(HomeView, self).get_context_data( *args, **kwargs )
        context ['products'] = Product.objects.all()
        return context
    
class PageDetail(generic.DetailView):    
    model = Page
    template = None
    def get_object(self):
        return get_object_or_404(
            Page,
            handle=self.kwargs['handle'],
        )
    def get_template_names(self):
        return [f'templates/{self.template}.html']