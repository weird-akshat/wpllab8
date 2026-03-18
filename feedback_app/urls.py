from django.urls import path

from . import views

urlpatterns = [
    path('', views.feedback_view, name='feedback-form'),
    path('thanks/', views.thanks_view, name='feedback-thanks'),
]
