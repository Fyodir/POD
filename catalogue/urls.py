from django.conf.urls import url
from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.index, name='index'),

    path('producttype/', views.ProductTypeView.as_view(), name='producttype'),
    path('producttype/<int:pk>', views.ProductTypeDetailView.as_view(), name='product-type-detail'),


    path('productinstance/', views.ProductInstanceListView.as_view(), name='productinstance'),
    path('productinstance/<uuid:pk>', views.ProductInstanceDetailView.as_view(), name='product-instance-detail'),
    path('producttype/<uuid:pk>/stock_update/', views.productinstance_stock_update, name='productinstance-stock-update'),


    path('supplier/', views.SupplierListView.as_view(), name='supplier'),
    path('supplier/<int:pk>', views.SupplierDetailView.as_view(), name='supplier-detail'),


    path('team/', views.TeamListView.as_view(), name='team'),
    path('team/<int:pk>', views.TeamDetailView.as_view(), name='team-detail'),

    path('order/', views.OrderListView.as_view(), name='order'),
    path('order/<int:pk>', views.OrderDetailView.as_view(), name='order-detail'),
    path('myorders/', views.OrdersCreatedByUserListView.as_view(), name='my-ordered'),


    path('requisition/', views.RequisitionListView.as_view(), name='requisition'),
    path('requisition/<int:pk>', views.RequisitionDetailView.as_view(), name='requisition-detail'),


    path('storage/', views.StorageListView.as_view(), name='storage'),
    path('storage/<int:pk>', views.StorageDetailView.as_view(), name='storage-detail'),

]
