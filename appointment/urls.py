
from django.urls import path
from .views import appointment

urlpatterns = [
    path('', appointment,name='appointment'),
]
