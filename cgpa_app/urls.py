from django.urls import path

from . import views

urlpatterns = [
    path('', views.cgpa_input_view, name='cgpa-input'),
    path('result/', views.cgpa_result_view, name='cgpa-result'),
]
