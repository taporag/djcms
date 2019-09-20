from django import template
from store.models import Product

register = template.Library()

@register.inclusion_tag('includes/product_grid.html')
def product_grid(products, **kwargs):
    if(kwargs.get('lg')):
        lg = kwargs.get('lg')
    else:
        lg = 3

    if(kwargs.get('md')):
        md = kwargs.get('md')
    else:
        md = 4
    
    if(kwargs.get('sm')):
        sm = kwargs.get('sm')
    else:
        sm = 6

    if(kwargs.get('xs')):
        xs = kwargs.get('xs')
    else:
        xs = 12

    column_classes = f'col-lg-{int(lg)} col-md-{int(md)} col-sm-{int(sm)} col-xs-{int(xs)}'
    return {
        'products': products,
        'column_classes': column_classes
    }

