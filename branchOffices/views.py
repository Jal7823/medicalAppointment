from django.contrib.auth.decorators import login_required, permission_required
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView

from .models import BranchOffices


class BranchOfficesDetail(DetailView):
    model = BranchOffices
    template_name = 'branchOffices/branchOfficesDetail.html'
    
    
    

class BranchOfficeList(ListView):
    # permission_required = ''
    model = BranchOffices
    template_name = 'branchOffices/branchOfficeList.html'

        
    def get_context_data(self, **kwargs):

        context = super(BranchOfficeList, self).get_context_data(**kwargs)
        context['branchOffice'] = BranchOffices.objects.all()
        return context
