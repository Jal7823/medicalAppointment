from django.urls import path
from .views import BranchOfficesDetail

urlpatterns = [
    path('detail/<int:pk>', BranchOfficesDetail.as_view(),name='detail'),
]
