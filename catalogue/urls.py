from django.conf.urls import url
from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('producttype/', views.ProductTypeView.as_view(), name='producttype'),
    path('producttype/<int:pk>', views.ProductTypeDetailView.as_view(), name='product-type-detail'),

    path('supplier/', views.SupplierListView.as_view(), name='supplier'),
    path('supplier/<int:pk>', views.SupplierDetailView.as_view(), name='supplier-detail'),
    # re_path(r'^supplier/(?P<primary_key>\d+)$', views.supplier_detail_view, name='supplier-detail'),

    path('team/', views.TeamListView.as_view(), name='team'),
    path('team/<int:pk>', views.TeamDetailView.as_view(), name='team-detail'),

    path('order/', views.OrderListView.as_view(), name='order'),

]
