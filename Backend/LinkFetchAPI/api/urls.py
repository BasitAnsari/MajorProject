from django.urls import path
from . import views

urlpatterns = [
    path('link-fetch/', views.linkFetch, name = 'link-fetch'),
]