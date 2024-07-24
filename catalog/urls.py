from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('order_list/', views.OrdersListView.as_view(), name='order_list'),
]