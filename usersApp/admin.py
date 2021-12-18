from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from import_export import fields, resources
from django.contrib.auth.models import Permission
from .models import Usuario



# ImportExportModelAdmin
class ResourcesUsuario(resources.ModelResource):
    class Meta:
        model = Usuario
        fields = '__all__'


class UsersAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    list_display = ('name','lastName','dni')
    list_filter = ('name','lastName','dni')
    resource_class = ResourcesUsuario


admin.site.register(Usuario,UsersAdmin)
admin.site.register(Permission)