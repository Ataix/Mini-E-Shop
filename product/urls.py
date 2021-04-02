from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from product.views import CategoryListView, ProductListView, ProductDetailView

urlpatterns = [
    path('categories/', CategoryListView.as_view(), name='category_list'),
    path('', ProductListView.as_view(), name='product_list'),
    path('product/<str:pk>/', ProductDetailView.as_view(), name='product_detail'),
]
