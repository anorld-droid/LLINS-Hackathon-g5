from  django.urls import path
from .import views

urlpatterns=[
    
    path('all',views.home,name='home'),
    path('states',views.states,name='states'),
    
]