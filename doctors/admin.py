from django.contrib import admin
from .models import Doctor,Patology,Specialty


class SpecialtyAdmin(admin.ModelAdmin):
    list_display = ('name',)

class DoctorsAdmin(admin.ModelAdmin):
    list_display = ('name','lastName',)
    list_filter = ('name','lastName',)

class PatologyAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_filter = ('name',)



admin.site.register(Doctor,DoctorsAdmin)
admin.site.register(Patology,PatologyAdmin)
admin.site.register(Specialty,SpecialtyAdmin)
