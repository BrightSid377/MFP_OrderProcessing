from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('catalog/order_list/', views.OrdersListView.as_view(), name='order_list'),

# mjl 7/30/2024 adding rows here for new order page
    path('order/create/', views.OrderCreate.as_view(), name='order_create'),
    path('order/<int:pk>/update/', views.OrderUpdate.as_view(), name='order_update'),

# mjl 7/31/2024 adding rows here for new staff and products page
    path('products/create/', views.ProductsCreate.as_view(), name='products_create'),
    path('products/<int:pk>/update/', views.ProductsUpdate.as_view(), name='products_update'),

    path('staff/create/', views.StaffCreate.as_view(), name='staff_create'),
    path('staff/<int:pk>/update/', views.StaffUpdate.as_view(), name='staff_update'),

]