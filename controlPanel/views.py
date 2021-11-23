from django.shortcuts import render,redirect
from django.views.generic import ListView,DetailView,UpdateView,DeleteView
from django.db.models import Q
from django.db.models import Avg, Max, Min, Sum
import datetime
from django.urls import reverse_lazy
from appointment.models import Appointment
from usersApp.models import Usuario
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.auth.decorators import permission_required,login_required
from django.core.exceptions import PermissionDenied
# Create your views here.

def controlPanelBase(request):
    return render(request, 'controlPanel/controlPanelBase.html')



def controlPanel(request):

    if request.user.isDoctor:

        # for counts
        countUser= Usuario.objects.all().count()
        sickUser = Usuario.objects.filter(
            Q(sick=True)
        ).count() 

        cured = Usuario.objects.filter(
            Q(sick=False)
        ).count() -1


        # for appointment
        date = datetime.datetime.now()
        fecha = date.strftime('%Y-%m-%d')
        appointmentToDay = Appointment.objects.filter(date=fecha).count()





        context = {
            'countUser':countUser,
            'sickUser':sickUser,
            'cured':cured,
            'appointmentMonth':appointmentToDay,
        }

        return render(request, 'controlPanel/controlPanel.html',context)
    else:
        return redirect(to='index')



class AppointmenToDay(ListView):
    model = Appointment
    template_name = "controlPanel/appointmentToDay.html"

    
    def get_context_data(self, **kwargs):
        context = super(AppointmenToDay, self).get_context_data(**kwargs)
    #for appointment today

        date = datetime.datetime.now()
        fecha = date.strftime('%Y-%m-%d')
        appointmentToDay = Appointment.objects.filter(date=fecha)


        #for appointment months

        rest = Appointment.objects.all()

        context['toDay'] =appointmentToDay
        context['rest'] =rest
        return context


class AppointmentListView(ListView):
    model = Appointment
    template_name = "controlPanel/appointmentList.html"
    
    
    def get_context_data(self, **kwargs):
        context = super(AppointmentListView, self).get_context_data(**kwargs)
        context['appointments'] = Appointment.objects.all()
        return context
    

    

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
    fields = ['name','lastName','dni','doctors','patology','sick','history']
    template_name = "controlPanel/patientsUpdate.html"
    success_url=reverse_lazy('PatientsListView')



def projections(request):
    users = Usuario.objects.all()
    context = {
        'users':users,
    }
    return render(request, 'controlPanel/projections.html',context)


class SicksListView(ListView):
    model = Usuario
    template_name = "controlPanel/sicksDetail.html"

    
    def get_context_data(self, **kwargs):
        context = super(SicksListView, self).get_context_data(**kwargs)
        sicks = Usuario.objects.filter(sick=True)
        context['sicks'] = sicks
        return context
    
class HealthyListView(ListView):
    model = Usuario
    template_name = "controlPanel/healthyDetail.html"

    
    def get_context_data(self, **kwargs):
        context = super(HealthyListView, self).get_context_data(**kwargs)
        healthy = Usuario.objects.filter(sick=False)
        context['healthy'] = healthy
        return context
