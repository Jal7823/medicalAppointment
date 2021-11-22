from django.contrib import admin
from .models import Simbolic

# Register your models here.


class SimbolicAdmin(admin.ModelAdmin):
    list_display = ('name',)


admin.site.register(Simbolic,SimbolicAdmin)