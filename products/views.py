from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormView
from .models import Product
from .forms import RegisterForm
from orders.forms import RegisterForm as OrderForm
from django.utils.decorators import method_decorator
from accounts.decorators import login_required
from rest_framework import generics
from rest_framework import mixins
from .serializers import ProductSerializer

class ProductListAPI(generics.GenericAPIView, mixins.ListModelMixin):
    serializer_class = ProductSerializer

    def get_queryset(self):
        return Product.objects.all().order_by('-id')

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

class ProductDetailAPI(generics.GenericAPIView, mixins.RetrieveModelMixin):
    serializer_class = ProductSerializer

    def get_queryset(self):
        return Product.objects.all().order_by('-id')

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

class ProductList(ListView):
    model = Product
    template_name = "product.html"
    context_object_name = 'product_list'

@method_decorator(login_required, name='dispatch')
class ProductRegister(FormView):
    template_name = "product_register.html"
    form_class = RegisterForm
    success_url = '/product/'

    def form_valid(self, form):
        product = Product(
                name = form.data.get('name'),
                price=form.data.get('price'),
                description=form.data.get('description'),
                stuck=form.data.get('stuck')
            )
        product.save()
        return super().form_valid(form)


class ProductDetail(DetailView):
    template_name = "product_detail.html"
    queryset = Product.objects.all()
    context_object_name = 'product'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = OrderForm(self.request)
        return context