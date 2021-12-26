from crispy_forms.utils import render_field
from django.contrib import admin
from import_export import fields, resources, widgets
from import_export.admin import ImportExportModelAdmin
from import_export.widgets import ManyToManyWidget

from doctors.models import Doctor

from .models import BranchOffices


class ResourcesBranchOffices(resources.ModelResource):
    doctors = fields.Field(attribute='doctors', widget=ManyToManyWidget(
        Doctor), column_name='doctors')

    class Meta:
        model = BranchOffices
        fields = ('name', 'address', 'phone', 'doctors')
        widget = ManyToManyWidget(Doctor, field='doctors')



class BranchOfficesAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('name',)
    list_filter = ('name',)
    resources_class = ResourcesBranchOffices


admin.site.register(BranchOffices, BranchOfficesAdmin)
