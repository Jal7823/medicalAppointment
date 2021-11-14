
from django.contrib import admin
from .models import Appointment



class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('id',)
    list_filter = ('id',)


admin.site.register(Appointment,AppointmentAdmin)


