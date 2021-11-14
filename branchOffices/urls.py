from django.urls import path
from .views import BranchOfficesDetail,BranchOfficeList

urlpatterns = [
    path('detail/<int:pk>', BranchOfficesDetail.as_view(),name='detail'),
    path('branchOffice', BranchOfficeList.as_view(),name='branchOffice'),
]
