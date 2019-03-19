from django.conf.urls import url
from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.index, name='index'),

    path('producttype/', views.ProductTypeView.as_view(), name='producttype'),
    path('producttype/<int:pk>', views.ProductTypeDetailView.as_view(), name='product-type-detail'),
    path('productype/create/', views.ProductTypeCreate.as_view(), name='product_type_create'),
    path('productype/<int:pk>/update/', views.ProductTypeUpdate.as_view(), name='product_type_update'),
    path('producttype/<int:pk>/delete/', views.ProductTypeDelete.as_view(), name='product_type_delete'),


    path('productinstance/', views.ProductInstanceListView.as_view(), name='productinstance'),
    path('productinstance/<uuid:pk>', views.ProductInstanceDetailView.as_view(), name='product-instance-detail'),
    path('producttype/<uuid:pk>/stock_update/', views.productinstance_stock_update, name='productinstance-stock-update'),
    path('productinstance/create/', views.ProductInstanceCreate.as_view(), name='productinstance_create'),
    path('productinstance/<uuid:pk>/update/', views.ProductInstanceUpdate.as_view(), name='productinstance_update'),
    path('productinstance/<uuid:pk>/delete/', views.ProductInstanceDelete.as_view(), name='productinstance_delete'),


    path('supplier/', views.SupplierListView.as_view(), name='supplier'),
    path('supplier/<int:pk>', views.SupplierDetailView.as_view(), name='supplier-detail'),
    path('supplier/create/', views.SupplierCreate.as_view(), name='supplier_create'),
    path('supplier/<int:pk>/update/', views.SupplierUpdate.as_view(), name='supplier_update'),
    path('supplier/<int:pk>/delete/', views.SupplierDelete.as_view(), name='supplier_delete'),


    path('team/', views.TeamListView.as_view(), name='team'),
    path('team/<int:pk>', views.TeamDetailView.as_view(), name='team-detail'),
    path('team/create/', views.TeamCreate.as_view(), name='team_create'),
    path('team/<int:pk>/update/', views.TeamUpdate.as_view(), name='team_update'),
    path('team/<int:pk>/delete/', views.TeamDelete.as_view(), name='team_delete'),


    path('order/', views.OrderListView.as_view(), name='order'),
    path('order/<int:pk>', views.OrderDetailView.as_view(), name='order-detail'),
    path('myorders/', views.OrdersCreatedByUserListView.as_view(), name='my-ordered'),
    path('order/create/', views.OrderCreate.as_view(), name='order_create'),
    path('order/<int:pk>/update/', views.OrderUpdate.as_view(), name='order_update'),
    path('order/<int:pk>/delete/', views.OrderDelete.as_view(), name='order_delete'),


    path('requisition/', views.RequisitionListView.as_view(), name='requisition'),
    path('requisition/<int:pk>', views.RequisitionDetailView.as_view(), name='requisition-detail'),
    path('requisition/create/', views.RequisitionCreate.as_view(), name='requisition_create'),
    path('requisition/<int:pk>/update/', views.RequisitionUpdate.as_view(), name='requisition_update'),
    # path('requisition/<int:pk>/updatesenior/', views.RequisitionUpdateAuthoriser.as_view(), name='requisition_update_authoriser'),
    path('requisition/<int:pk>/delete/', views.RequisitionDelete.as_view(), name='requisition_delete'),


    path('storage/', views.StorageListView.as_view(), name='storage'),
    path('storage/<int:pk>', views.StorageDetailView.as_view(), name='storage-detail'),
    path('storage/create/', views.StorageCreate.as_view(), name='storage_create'),
    path('storage/<int:pk>/update/', views.StorageUpdate.as_view(), name='storage_update'),
    path('storage/<int:pk>/delete/', views.StorageDelete.as_view(), name='storage_delete'),

    path('temperature/', views.TemperatureListView.as_view(), name='temperature'),
    path('temperature/<int:pk>', views.TemperatureDetailView.as_view(), name='temperature-detail'),
    path('temperature/create/', views.TemperatureCreate.as_view(), name='temperature_create'),
    path('temperature/<int:pk>/update/', views.TemperatureUpdate.as_view(), name='temperature_update'),
    path('temperature/<int:pk>/delete/', views.TemperatureDelete.as_view(), name='temperature_delete'),

]
