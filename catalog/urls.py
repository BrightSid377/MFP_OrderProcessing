from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('catalog/order_list/', views.OrdersListView.as_view(), name='order_list'),

# mjl 7/30/2024 adding rows here for new order page
    path('order/create/', views.OrderCreate.as_view(), name='order_create'),
    path('order/<int:pk>/update/', views.OrderUpdate.as_view(), name='order_update'),

]