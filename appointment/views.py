from locale import format

from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.models import User
from django.db.models import Q
from django.shortcuts import redirect, render
from django.views.generic import DetailView, ListView,DeleteView

from usersApp.models import Usuario

from .forms import formsAppointment
from .models import Appointment


@login_required(login_url='login')
def appointment(request):
    appointment = Appointment.objects.all()
    title = 'Citas Medicas'


    if request.method == 'POST':
        form = formsAppointment(request.POST)
        if form.is_valid():
            form.save()
        return redirect(to='appointmentList')
    else:
        form = formsAppointment()


    context = {
        'form':form,    
        'title':title,
    }

    return render(request, 'appointment/appointment.html',context)

def appointmentList(request):
    userActivate = request.user.id

    filterUser = Appointment.objects.filter(
        Q(user_id = userActivate)
    )


    context={
        'userActivate':userActivate,
        'filterUser':filterUser,

    }

    return render(request, 'appointment/appointmentDetail.html',context)



class AppointmentDeleteView(DeleteView):
    model = Appointment
    template_name = "appointment/appointmentDelete.html"
    success_url='/'
