from django.contrib.auth.decorators import login_required, permission_required
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView

from .models import BranchOffices


class BranchOfficesDetail(DetailView):
    """Should be get detail of BranchOffices

    Return:
        DetailView (dic): It have all information of BranchOffices, it's class for any field of data base of this models, you can access to any field of this model through to dot methodology.
            Example:
                object.name
                object.address
    """    
    model = BranchOffices
    template_name = 'branchOffices/branchOfficesDetail.html'
    
class BranchOfficeList(ListView):
    """Should be get list of BranchOffices

    Returns:
        branchOffice: list of BranchOffices
    """    
    model = BranchOffices
    template_name = 'branchOffices/branchOfficeList.html'

        
    def get_context_data(self, **kwargs):

        context = super(BranchOfficeList, self).get_context_data(**kwargs)
        context['branchOffice'] = BranchOffices.objects.all()
        return context
