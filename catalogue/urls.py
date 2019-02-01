from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('producttype/', views.ProductTypeView.as_view(), name='producttype'),
]
