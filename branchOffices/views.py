from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic.detail import DetailView
from django.db.models import Q


from .models import BranchOffices


class BranchOfficesDetail(DetailView):
    model = BranchOffices
    template_name = 'branchOffices/branchOfficesDetail.html'
    

