from django.urls import path
from .views import detailSpecialty,error404

urlpatterns = [
    path('detailSpecialty/<int:id>',detailSpecialty,name='detailSpecialty'),
    path('error404/',error404,name='erro404')
]
