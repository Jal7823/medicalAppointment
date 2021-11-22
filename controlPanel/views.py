from django.shortcuts import render
from django.views.generic import ListView,DetailView,UpdateView,DeleteView
from django.db.models import Q
from django.db.models import Avg, Max, Min, Sum
import datetime

from appointment.models import Appointment
from usersApp.models import Usuario
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.auth.decorators import permission_required,login_required
# Create your views here.

def controlPanel(request):
    # for counts
    countUser= Usuario.objects.all().count()
    sickUser = Usuario.objects.filter(
        Q(sick=True)
    ).count()

    cured = Usuario.objects.filter(
        Q(sick=False)
    ).count()


    # for appointment

    #for appointment today

    date = datetime.datetime.now()
    fecha = date.strftime('%Y-%m-%d')
    appointmentToDay = Appointment.objects.filter(date=fecha)
    appointmentDiferentDay = Appointment.objects.filter(
        ~Q(date=fecha)
    )
    appointmentCountToDay = Appointment.objects.filter(date=fecha).count()


    #for appointment months

    appointmentMonth = Appointment.objects.all()


    context = {
        'countUser':countUser,
        'sickUser':sickUser,
        'cured':cured,
        'appointmentToDay':appointmentToDay,
        'appointmentCountToDay':appointmentCountToDay,
        'appointmentMonth':appointmentMonth,
        'appointmentDiferentDay':appointmentDiferentDay,
    }

    return render(request, 'controlPanel/controlPanel.html',context)



class PatientsListView(ListView):
    model = Appointment
    template_name = "controlPanel/patientsList.html"
    
    
    def get_context_data(self, **kwargs):
        context = super(PatientsListView, self).get_context_data(**kwargs)
        context['usersAppointment'] = Appointment.objects.all()
        return context
    

class PatientDetailView(DetailView):
    model = Usuario
    template_name = "controlPanel/patientsDetail.html"



class UsersUpdateView(UpdateView):
    model = Usuario
    fields = ['name','lastName','dni','doctors','exam','patology','history']
    template_name = "controlPanel/patientsUpdate.html"
    success_url='/'



