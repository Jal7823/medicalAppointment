from django.shortcuts import render,redirect
from .forms import formsAppointment
from .models import Appointment


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