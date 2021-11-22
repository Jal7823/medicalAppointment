
from django.urls import path
from .views import appointment,appointmentList,AppointmentDeleteView

urlpatterns = [
    path('', appointment,name='appointment'),
    path('appointmentList/', appointmentList,name='appointmentList'),
    path('appointmentDeleteView/<int:pk>', AppointmentDeleteView.as_view(),name='AppointmentDeleteView'),
]
