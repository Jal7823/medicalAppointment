from django.urls import path
from .views import detailSpecialty,error404,about

urlpatterns = [
    path('detailSpecialty/<int:id>',detailSpecialty,name='detailSpecialty'),
    path('error404/',error404,name='erro404'),
    path('about/',about,name='about')
]
