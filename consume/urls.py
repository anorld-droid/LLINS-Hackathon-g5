from  django.urls import path
from .import views

urlpatterns=[

    path('dashboard',views.dashboard,name='dashboard'),
    path('kisumu',views.kisumu,name='kisumu'),
    path('vihiga',views.vihiga,name='vihiga'),
    path('busia',views.busia,name='busia'),
    
]