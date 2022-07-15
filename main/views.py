from django.http import Http404
from django.shortcuts import render
from django.views import View

from .models import Product


def product_list(request):
    products = Product.objects.all()
    # {'search': 'iphone'}
    value = request.GET.get('search')
    if value:
        products = products.filter(name__icontains=value)
    return render(request, 'main/list.html', {'products': products})


class ProductDetailsView(View):
    def get(self, request, product_id):
        try:
            product = Product.objects.get(id=product_id)
            return render(request, 'main/details.html', {'product': product})
        except Product.DoesNotExist:
            raise Http404
