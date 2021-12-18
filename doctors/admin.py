from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from import_export import fields, resources
from .models import Doctor, Patology, Specialty


# ImportExportModelAdmin
class ResourcesSpecialtyAdmin(resources.ModelResource):
    class Meta:
        model = Specialty
        fields = '__all__'


class ResourcesDoctorsAdmin(resources.ModelResource):
    class Meta:
        model = Doctor
        fields = '__all__'


class ResourcesPatologyAdmin(resources.ModelResource):
    class Meta:
        model = Patology
        fields = '__all__'


class SpecialtyAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    list_display = ('name',)


class DoctorsAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    list_display = ('name', 'lastName',)
    list_filter = ('name', 'lastName',)


class PatologyAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    list_display = ('name',)
    list_filter = ('name',)


admin.site.register(Doctor, DoctorsAdmin)
admin.site.register(Patology, PatologyAdmin)
admin.site.register(Specialty, SpecialtyAdmin)
