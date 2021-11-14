from django.urls import path
from .views import detailSpecialty

urlpatterns = [
    path('detailSpecialty/<int:id>',detailSpecialty,name='detailSpecialty')
]
