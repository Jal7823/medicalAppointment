from django.urls import path
from .views import controlPanel,PatientsListView,PatientDetailView

urlpatterns =[
    path('',controlPanel,name='controlPanel'),
    path('PatientsListView/',PatientsListView.as_view(),name='PatientsListView'),
    path('PatientDetailView/<int:pk>',PatientDetailView.as_view(),name='PatientDetailView'),
]