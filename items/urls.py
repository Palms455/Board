from django.contrib import admin
from django.conf import settings
from django.urls import path , include
from .views import ItemList, CategoryList, CategoryDetail, ItemDetail, SellerDetail

urlpatterns = [
    path('', ItemList.as_view(), name='item_list_url' ),
   
    path('category/', CategoryList.as_view(), name= 'category_list_url'),
    path('category/<int:pk>/', CategoryDetail.as_view(), name='category_detail_url'),
    path('item/<int:pk>/', ItemDetail.as_view(), name= 'item_detail_url'),
    path('seller/<int:pk>/', SellerDetail.as_view(), name= 'seller_detail_url'),
]

