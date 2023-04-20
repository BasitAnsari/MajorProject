from django.contrib import admin
from django.urls import path
from django.conf.urls import include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/link/', include('links.urls')),
    path('api/summarizer/', include('summarizer.urls')),
]