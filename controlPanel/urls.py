from django.urls import path
from .views import controlPanel

urlpatterns =[
    path('',controlPanel,name='controlPanel')
]