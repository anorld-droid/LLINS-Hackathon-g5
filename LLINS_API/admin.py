from django.contrib import admin
from LLINS_API.models import Patients, Net

# Register your models here.


class PatientsAdmin(admin.ModelAdmin):
    list_display = ("County", "SubCounty", "Year", "Month")


class NetAdmin(admin.ModelAdmin):
    list_display = ("County", "SubCounty", "Year", "Month")


admin.site.register(Patients, PatientsAdmin)
admin.site.register(Net, NetAdmin)
