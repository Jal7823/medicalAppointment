from django.contrib.auth.mixins import PermissionRequiredMixin
from django.db.models import Q
from django.shortcuts import render

from branchOffices.models import BranchOffices
from doctors.models import Doctor, Specialty


def index(request):
    branchOffices = BranchOffices.objects.all()[:4]
    specialty = Specialty.objects.all()
    doctors = Doctor.objects.all()

    context = {
        'branchOffices':branchOffices,
        'specialty':specialty,
        'doctors':doctors,
    }
    return render(request, 'index.html', context)


def error404(request):
    return render(request, 'error404.html')




def detailSpecialty(request,id):
    specialtyQuery = Specialty.objects.get(id=id)
    branchOffices = BranchOffices.objects.filter(
        Q(specialty__name__icontains = specialtyQuery ),
    )
    context = {
        'branchOffices':branchOffices,
    }

    return render(request, 'branchOffices/specialtyFilter.html',context)


def about(request):
    title = 'Sobre nosotros'
    context = {
        'title':title,
    }
    return render(request, 'about.html',context)



