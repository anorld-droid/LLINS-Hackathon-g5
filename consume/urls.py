from  django.urls import path
from .import views

urlpatterns=[

    path('combined',views.combined,name='combined'),
    path('states',views.states,name='states'),
    path('dashboard',views.dashboard,name='dashboard'),
    
]