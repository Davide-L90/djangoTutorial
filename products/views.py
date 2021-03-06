# from django.views.generic.detail import DetailView
# from django.views.generic.list import ListView

from products.models import Product
from django.http import JsonResponse

# class ProductDetailView(DetailView):
#     model = Product
#     template_name = "products/product_detail.html"
#
#
# class ProductListView(ListView):
#     model = Product
#     template_name = "products/product_list.html"


def product_list(request):
    products = Product.objects.all()
    data = {'products': list(products.values())}
    response = JsonResponse(data)
    return response


def product_detail(request, pk):
    try:
        product = Product.objects.get(pk=pk)
        data = {
            'name': product.name,
            'manufacturer': product.manufacturer.name,
            'description': product.description,
            'photo': product.photo.url,
            'price': product.price,
            'shipping_cost': product.shipping_cost,
            'quantity': product.quantity,
        }
        response = JsonResponse(data)
        return response
    except Product.DoesNotExist:
        response = JsonResponse({
            'error': {
                'code': 404,
                'message': 'No product found'
            }},
            status=404
        )
        return response
