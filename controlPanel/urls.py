from django.urls import path
from django.contrib.auth.decorators import permission_required,login_required
from .views import controlPanel,PatientsListView,PatientDetailView,UsersUpdateView,controlPanelBase,projections,SicksListView,HealthyListView,AppointmenToDay,AppointmentListView,SicksList,CuredList


urlpatterns =[
    path('', controlPanel,name='controlPanel'),
    path('controlPanelBase/', controlPanelBase,name='controlPanelBase'),
    path('projections/', projections,name='projections'),
    path('AppointmenToDay/',AppointmenToDay.as_view(),name='AppointmenToDay'),
    path('AppointmentListView/',AppointmentListView.as_view(),name='AppointmentListView'),
    path('SicksDetail/',SicksListView.as_view(),name='SicksDetail'),
    path('HealthyListView/',HealthyListView.as_view(),name='HealthyListView'),
    path('SicksList/',SicksList.as_view(),name='SicksList'),
    path('CuredList/',CuredList.as_view(),name='CuredList'),
    path('PatientDetailView/<int:pk>',PatientDetailView.as_view(),name='PatientDetailView'),
    path('PatientsListView/',PatientsListView.as_view(),name='PatientsListView'),
    path('UsersUpdateView/<int:pk>',UsersUpdateView.as_view(),name='UsersUpdateView'),

]