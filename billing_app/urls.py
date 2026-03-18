from django.urls import path

from . import views

urlpatterns = [
    path('', views.order_view, name='billing-order'),
    path('bill/', views.bill_view, name='billing-bill'),
]
