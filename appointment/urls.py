
from django.urls import path
from .views import appointment#AppointmentDetail

urlpatterns = [
    path('', appointment,name='appointment'),
    # path('appointmentList/', AppointmentDetail,name='appointmentDetail'),
]
