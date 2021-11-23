from django.contrib.auth.decorators import login_required, permission_required
from django.urls import path

from .views import (AppointmentListView, AppointmenToDay, HealthyListView,
                    PatientDetailView, PatientsListView, SicksListView,
                    UsersUpdateView, controlPanel, controlPanelBase,
                    projections)

urlpatterns =[
    path('',controlPanel,name='controlPanel'),
    path('controlPanelBase/', controlPanelBase,name='controlPanelBase'),
    path('projections/', projections,name='projections'),
    path('PatientsListView/',PatientsListView.as_view(),name='PatientsListView'),
    path('AppointmenToDay/',AppointmenToDay.as_view(),name='AppointmenToDay'),
    path('AppointmentListView/',AppointmentListView.as_view(),name='AppointmentListView'),
    path('SicksListView/',SicksListView.as_view(),name='SicksListView'),
    path('HealthyListView/',HealthyListView.as_view(),name='HealthyListView'),
    path('PatientDetailView/<int:pk>',PatientDetailView.as_view(),name='PatientDetailView'),
    path('UsersUpdateView/<int:pk>',UsersUpdateView.as_view(),name='UsersUpdateView'),
]