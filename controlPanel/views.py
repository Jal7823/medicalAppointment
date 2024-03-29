import datetime
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.core.exceptions import PermissionDenied
from django.db.models import Avg, Max, Min, Q, Sum
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import DeleteView, DetailView, ListView, UpdateView,CreateView
from django.core.paginator import Paginator
#internals
from appointment.models import Appointment
from usersApp.models import Usuario
from doctors.models import Doctor,Specialty
from .forms import CreateMedicForms,UpdatePatient,CreatePatient

# Create your views here.

def controlPanelBase(request):
    cured = Usuario.objects.filter(
        Q(sick=False)&
        Q(isDoctor = False)
    )

    sick = Usuario.objects.filter(
    Q(sick=True)&
    Q(isDoctor = False)
    )
    patients = Usuario.objects.filter(
        Q(sick=True) &
        Q(isDoctor = False)
    )
    patientsCount = Usuario.objects.filter(
    Q(isDoctor = False)
    ).count()

    specialty = Specialty.objects.all()

    context = {
        'cured':cured,
        'sick':sick,
        'patients':patients,
        'patientsCount':patientsCount,
        'specialty':specialty,

    }
    return render(request, 'controlPanel/controlPanelBase.html',context)

def controlPanel(request):

    if request.user.isDoctor or request.user.user_administrator:

        # for counts
        countUser= Usuario.objects.filter(
            Q(user_administrator=False)
        ).count()

        sickUser = Usuario.objects.filter(
            Q(sick=True) &
            Q(isDoctor = False)&
            Q(user_administrator=False)
        ).count() 

        cured = Usuario.objects.filter(
            Q(sick=False) &
            Q(isDoctor = False)&
            Q(user_administrator=False)
        ).count() 

        # for appointment
        date = datetime.datetime.now()
        fecha = date.strftime('%Y-%m-%d')
        appointmentToDay = Appointment.objects.filter(date=fecha).count()

        if appointmentToDay:
            patientsAll = Usuario.objects.filter(
            Q(isDoctor = False)
            )

        else:
            patientsAll = Usuario.objects.filter(
                Q(isDoctor=False)
            )[:6]

        #for graph
        data = [23,30,80,75,37,13,98,65,34,45,38,87]

        context = {
            'countUser':countUser,
            'sickUser':sickUser,
            'cured':cured,
            'appointmentMonth':appointmentToDay,
            'patientsAll':patientsAll,
            'data':data,
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

    def dispatch(self, request, *args, **kwargs):
        if request.user.isDoctor or request.user.user_administrator:
            return super(AppointmenToDay, self).dispatch(request, *args, **kwargs)
        else:    
            return redirect(to='index')

class AppointmentListView(ListView):
    model = Appointment
    template_name = "controlPanel/appointmentList.html"
    
    
    def get_context_data(self, **kwargs):
        context = super(AppointmentListView, self).get_context_data(**kwargs)
        context['appointments'] = Appointment.objects.all()
        return context

    def dispatch(self, request, *args, **kwargs):
        if request.user.isDoctor or request.user.user_administrator:
            return super(AppointmentListView, self).dispatch(request, *args, **kwargs)
        else:    
            return redirect(to='index')

class PatientsListView(ListView):
    model = Appointment
    template_name = "controlPanel/patientsList.html"
    
    
    def get_context_data(self, **kwargs):
        context = super(PatientsListView, self).get_context_data(**kwargs)
        context['usersAppointment'] = Usuario.objects.filter(
            Q(user_administrator=False)&
            Q(isDoctor=False)

        )
        return context

    
    def dispatch(self, request, *args, **kwargs):
        if request.user.isDoctor or request.user.user_administrator:
            return super(PatientsListView, self).dispatch(request, *args, **kwargs)
        else:    
            return redirect(to='index')

class PatientDetailView(DetailView):
    model = Usuario
    template_name = "controlPanel/patientsDetail.html"
    
    def get_context_data(self, **kwargs):
        context = super(PatientDetailView, self).get_context_data(**kwargs)
        return context


    def dispatch(self, request, *args, **kwargs):
        if request.user.isDoctor or request.user.user_administrator:
            return super(PatientDetailView, self).dispatch(request, *args, **kwargs)
        else:    
            return redirect(to='index')

class UsersUpdateView(UpdateView):
    model = Usuario
    template_name = "controlPanel/patientsUpdate.html"
    form_class =UpdatePatient
    success_url=reverse_lazy('PatientsListView')

    def dispatch(self, request, *args, **kwargs):
        if request.user.isDoctor or request.user.user_administrator:
            return super(UsersUpdateView, self).dispatch(request, *args, **kwargs)
        else:    
            return redirect(to='index')

class CreatePatient(CreateView):
    model = Usuario
    form_class = CreatePatient
    template_name = 'controlPanel/createPatient.html'
    success_url = reverse_lazy('controlPanel')
def projections(request):

    if request.user.isDoctor or request.user.user_administrator:

        users = Usuario.objects.all()
        context = {
            'users':users,
        }
        return render(request, 'controlPanel/projections.html',context)
    else:
        return redirect(to='index')

class SicksListView(ListView):
    model = Usuario
    template_name = "controlPanel/sicksDetail.html"

    
    def get_context_data(self, **kwargs):
        context = super(SicksListView, self).get_context_data(**kwargs)
        sicks = Usuario.objects.filter(sick=True)

        context['sicks'] = sicks
        return context

    def dispatch(self, request, *args, **kwargs):
        if request.user.isDoctor or request.user.user_administrator:
            return super(SicksListView, self).dispatch(request, *args, **kwargs)
        else:    
            return redirect(to='index')

class HealthyListView(ListView):
    model = Usuario
    template_name = "controlPanel/healthyDetail.html"

    
    def get_context_data(self, **kwargs):
        context = super(HealthyListView, self).get_context_data(**kwargs)
        healthy = Usuario.objects.filter(sick=False)
        context['healthy'] = healthy
        return context

    def dispatch(self, request, *args, **kwargs):
        if request.user.isDoctor or request.user.user_administrator:
            return super(HealthyListView, self).dispatch(request, *args, **kwargs)
        else:    
            return redirect(to='index')

class SicksList(ListView):
    model = Usuario
    template_name = 'controlPanel/sicksList.html'

    
    def get_context_data(self, **kwargs):
        context = super(SicksList, self).get_context_data(**kwargs)
        context['patients'] = Usuario.objects.filter(
            Q(sick = True) &
            Q(isDoctor = False)
        )
        return context
    
class CuredList(ListView):
    model = Usuario
    template_name = 'controlPanel/curedList.html'

    
    def get_context_data(self, **kwargs):
        context = super(CuredList, self).get_context_data(**kwargs)
        context['patients'] = Usuario.objects.filter(
            Q(sick = False ) &
            Q(isDoctor = False)
        )
        return context

