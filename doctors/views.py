from django.contrib.auth.mixins import PermissionRequiredMixin
from django.db.models import Q
from django.shortcuts import render

from branchOffices.models import BranchOffices
from doctors.models import Doctor, Specialty


def index(request):
    """Should be list all doctors, spacielies and branch offices

    Returns:
        dict: context{
            'branchOffices': List of all branch offices,
            'specialty': List of all specialties,
            'doctors': List of all doctors,

        } 
    """    
    branchOffices = BranchOffices.objects.all()[:4]
    specialty = Specialty.objects.all()[:6]
    doctors = Doctor.objects.all()

    context = {
        'branchOffices': branchOffices,
        'specialty': specialty,
        'doctors': doctors,
    }
    return render(request, 'index.html', context)


def error404(request):
    return render(request, 'error404.html')

def detailSpecialty(request, id):
    """Should be filter the branch offices per specialties

    Args:
        request: request
        id (int): identifier od branch office

    Returns:
        dict: context{
         'branchOffices': branchOffices,
        }
    """    
    specialtyQuery = Specialty.objects.get(id=id)
    branchOffices = BranchOffices.objects.filter(
        Q(specialty__name__icontains=specialtyQuery),
    )
    context = {
        'branchOffices': branchOffices,
    }

    return render(request, 'branchOffices/specialtyFilter.html', context)

def about(request):
    
    title = 'Sobre nosotros'
    context = {
        'title': title,
    }
    return render(request, 'about.html', context)
