from django.contrib import admin
from .models import BranchOffices


class BranchOfficesAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_filter = ('name',)




admin.site.register(BranchOffices,BranchOfficesAdmin)
