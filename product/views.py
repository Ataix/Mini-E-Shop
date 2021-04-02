from django.urls import reverse
from django.views.generic import ListView, DetailView, CreateView

from product.forms import ProductForm
from product.models import Category, Product


class CategoryListView(ListView):
    model = Category
    template_name = 'product/category_list.html'


class CategoryDetailView(DetailView):
    model = Category
    template_name = 'product/category_detail.html'


class ProductListView(ListView):
    model = Product
    template_name = 'product/product_list.html'


class ProductDetailView(DetailView):
    model = Product
    template_name = 'product/product_detail.html'
