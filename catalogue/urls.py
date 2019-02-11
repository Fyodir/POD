from django.conf.urls import url
from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('producttype/', views.ProductTypeView.as_view(), name='producttype'),
    path('producttype/<int:pk>', views.ProductTypeDetailView.as_view(), name='product-type-detail'),
    path('supplier/', views.SupplierView.as_view(), name='supplier'),
    re_path(r'^supplier/(?P<primary_key>\d+)$', views.supplier_detail_view, name='supplier-detail'),
]
