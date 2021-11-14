from django.shortcuts import render
from branchOffices.models import BranchOffices
from doctors.models import Specialty,Doctor
from branchOffices.models import BranchOffices
from django.db.models import Q

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



def detailSpecialty(request,id):
    specialtyQuery = Specialty.objects.get(id=id)
    branchOffices = BranchOffices.objects.filter(
        Q(specialty__name__icontains = specialtyQuery ),
    )
    context = {
        'branchOffices':branchOffices,
    }

    print(specialtyQuery)
    print(branchOffices)

    return render(request, 'branchOffices/specialtyFilter.html',context)
