from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from import_export import fields, resources
from .models import BranchOffices


class ResourcesBranchOffices(resources.ModelResource):
    class Meta:
        model = BranchOffices
        fields = '__all__'


class BranchOfficesAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('name',)
    list_filter = ('name',)
    resources_class = ResourcesBranchOffices


admin.site.register(BranchOffices, BranchOfficesAdmin)
