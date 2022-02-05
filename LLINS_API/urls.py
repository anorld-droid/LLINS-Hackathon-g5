from django.urls import path
from LLINS_API import views
from rest_framework.urlpatterns import format_suffix_patterns
from django.contrib import admin
urlpatterns = [
    path('', admin.site.urls),
    path('patients/', views.patient_data_list),
    path('patints/<int:pk>/', views.patient_data_detail),
    path('nets/', views.nets_list),
]
