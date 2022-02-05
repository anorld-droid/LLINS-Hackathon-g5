"""LLINS_Hackathon_g5 URL Configuration"""

from django.urls import path, include

urlpatterns = [
    path('', include('LLINS_API.urls')),
]
