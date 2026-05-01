from django.urls import path
from . import views

urlpatterns = [
    path('', views.service_list, name='service_list'),
    path('services/<int:pk>/', views.service_detail, name='service_detail'),
    path('contacts/', views.contacts, name='contacts'),
    path('devices/', views.device_list, name='device_list'),
    path('devices/add/', views.device_create, name='device_create'),
    path('devices/<int:pk>/delete/', views.device_delete, name='device_delete'),
    path('orders/', views.order_list, name='order_list'),
    path('orders/new/', views.order_create, name='order_create'),
    path('orders/<int:pk>/', views.order_detail, name='order_detail'),
]