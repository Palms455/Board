from django.contrib import admin
from django.conf import settings
from django.urls import path , include
from .views import ItemList, CategoryList, CategoryDetail, ItemDetail, SellerDetail, AddCategory, AddItem, ItemUpdate, CategoryUpdate, CategoryDelete, ItemDelete

urlpatterns = [
	path('seller/<int:pk>/', SellerDetail.as_view(), name= 'seller_detail_url'),
    path('addcategory/', AddCategory.as_view(), name='add_category_url'),
    path('category/', CategoryList.as_view(), name= 'category_list_url'),
    path('category/<int:pk>/', CategoryDetail.as_view(), name='category_detail_url'),
    path('category/<int:pk>/update/', CategoryUpdate.as_view(), name='category_update_url'),
    path('category/<int:pk>/delete/', CategoryDelete.as_view(), name='category_delete_url'),
    path('', ItemList.as_view(), name='item_list_url' ),
    path('item/<int:pk>/', ItemDetail.as_view(), name= 'item_detail_url'),
    path('item/<int:pk>/update/', ItemUpdate.as_view(), name= 'item_update_url'),
    path('additem/', AddItem.as_view(), name='add_item_url'),
    path('item/<int:pk>/delete/', ItemDelete.as_view(), name='item_delete_url'),

    
]

