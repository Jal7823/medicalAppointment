from django.shortcuts import render,redirect
from django.views.generic import DetailView,ListView
from django.db.models import Q
from django.contrib.auth.decorators import login_required,permission_required

from .forms import formsAppointment
from .models import Appointment
from django.contrib.auth.models import User




@login_required(login_url='login')
def appointment(request):
    appointment = Appointment.objects.all()
    title = 'Citas Medicas'

    if request.method == 'POST':
        form = formsAppointment(request.POST)
        if form.is_valid():
            form.save()
        return redirect(to='appointment')
    else:
        form = formsAppointment()


    context = {
        'form':form,    
        'title':title,
    }

    return render(request, 'appointment/appointment.html',context)

# def AppointmentDetail(request):
#     userActive = User.id
#     appointment = Appointment.objects.get(
#         Q(id=userActive),
#     )    

#     context = {
#         'appointment':appointment,
#     }
#     print('==>',userActive)

#     return render(request,'appointment/appointmentDetail.html',context)

    
