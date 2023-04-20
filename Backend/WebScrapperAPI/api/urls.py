from django.urls import path
from . import views

urlpatterns = [
    path('get-text/', views.getText, name = 'get-text'),
]