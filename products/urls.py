""" This file contains the urls needed in the products app """
from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_products, name='products'),
    path('prints/', views.all_prints, name='prints'),
    path('frames/', views.all_frames, name='frames'),
    path('<int:product_id>/', views.product_detail, name='product_detail'),
    path('add/', views.add_product, name='add_product'),
    path('edit/<int:product_id>/', views.edit_product, name='edit_product'),
    path('delete/<int:product_id>/',
         views.delete_product, name='delete_product'),
]
