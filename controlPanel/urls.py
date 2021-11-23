from django.urls import path
from django.contrib.auth.decorators import permission_required,login_required
from .views import controlPanel,PatientsListView,PatientDetailView,UsersUpdateView,controlPanelBase,projections


urlpatterns =[
    path('controlPanelBase/', controlPanelBase,name='controlPanelBase'),
    path('projections/', projections,name='projections'),
    path('', controlPanel,name='controlPanel'),
    path('PatientsListView/',PatientsListView.as_view(),name='PatientsListView'),
    path('PatientDetailView/<int:pk>',PatientDetailView.as_view(),name='PatientDetailView'),
    path('UsersUpdateView/<int:pk>',UsersUpdateView.as_view(),name='UsersUpdateView'),
]