from django.urls import reverse
from django.conf import settings
from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, ListView, DetailView, View, UpdateView

from allauth.account.decorators import verified_email_required

from .forms import ProductUpdateForm
from product.models import Product, Order
from .serializers import ProductSerializer, OrderSerializer

import json
from rest_framework import viewsets


class ProductDetail(DetailView):
    '''
    product detail class
    '''
    model = Product
    context_object_name = 'product'

product_detail = ProductDetail.as_view()

class ProductsList(ListView):
    '''
    product view list class
    '''
    model = Product
    success_url = '/charge'

    @method_decorator(verified_email_required)
    def dispatch(self, *args, **kwargs):
        return super(ProductsList, self).dispatch(*args, **kwargs)

    def get_context_data(self, **kwargs):

        context = super(ProductsList, self).get_context_data(**kwargs)
        if self.request.user.role == 'admin':
            list_of_product = Product.objects.filter(user=self.request.user)
            context['list_of_product'] = list_of_product

        else:
            list_of_product = Product.objects.all()
            context['list_of_product'] = list_of_product
            context['key'] = settings.STRIPE_PUBLISHABLE_KEY

        return context

product_list = ProductsList.as_view()


class ProductCreate(CreateView):
    '''
    product create class
    '''
    model = Product
    fields = ['product_name', 'description', 'price', 'image']
    success_url = '/'

    @method_decorator(verified_email_required)
    def dispatch(self, *args, **kwargs):
        return super(ProductCreate, self).dispatch(*args, **kwargs)

    def form_valid(self, form):
        ''' form '''
        obj = form.save(commit=False)
        obj.user = self.request.user
        obj.save()
        return super(ProductCreate, self).form_valid(form)


product_create = ProductCreate.as_view()


class ProductDelete(View):
    """
    product delete class
    """
    def  get(self, request):
        ''' get data '''
        id = request.GET.get('id', None)
        Product.objects.get(id=id).delete()
        data = {
            'deleted': True
        }
        return JsonResponse(data)

product_delete = ProductDelete.as_view()

class UpdateProduct(UpdateView):
    """
    Updating product through AJAX
    """

    model = Product
    fields = ['product_name', 'description', 'price', 'image']

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = str(self.get_form())
        return JsonResponse({'form': form})

    def form_valid(self, form):
        """If the form is valid, save the associated model."""
        self.object = form.save()
        return JsonResponse({'data': 'success'})

product_update = UpdateProduct.as_view()

def purchased_view(request, pk):
    ''' purchased  '''
    order = Order()
    order.product = Product.objects.get(id=pk)
    order.user = request.user
    order.price = order.product.price
    order.save()
    return render(request, 'product/charge.html')


class PurchasedHistory(ListView):
    model = Order
    context_object_name = 'buyed_products'

    def get_queryset(self):
        return self.model.objects.filter(user=self.request.user)

product_order = PurchasedHistory.as_view()



class ProductView(viewsets.ModelViewSet):
    Queryset = Product.objects.all()
    def get_queryset(self):
        user = self.request.user
        return Product.objects.all()
    serializer_class = ProductSerializer