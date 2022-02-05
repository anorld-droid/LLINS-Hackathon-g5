"""LLINS_Hackathon_g5 URL Configuration"""

from django.urls import path, include

urlpatterns = [
    
    path('charts/', include('consume.urls')),
    path('', include('LLINS_API.urls')),



    
]
