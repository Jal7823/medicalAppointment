
from django.urls import path
from .views import appointment,appointmentList

urlpatterns = [
    path('', appointment,name='appointment'),
    path('appointmentList/', appointmentList,name='appointmentDetail'),
]
