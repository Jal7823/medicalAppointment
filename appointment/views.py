from django.shortcuts import render,redirect
from django.views.generic import DetailView,ListView
from django.db.models import Q
from django.contrib.auth.decorators import login_required,permission_required

from .forms import formsAppointment
from .models import Appointment
from django.contrib.auth.models import User
from usersApp.models import Usuario




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

def appointmentList(request):
    usuariocita = Appointment.objects.all()
    usuarioactivo = request.user.username
    context={
        'usuariocita':usuariocita,
        'usuarioactivo':usuarioactivo,
    }

    return render(request, 'appointment/appointmentDetail.html',context)


