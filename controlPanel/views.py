from django.shortcuts import render
from django.views.generic import ListView,DetailView,UpdateView
from appointment.models import Appointment
from usersApp.models import Usuario
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.auth.decorators import permission_required,login_required
# Create your views here.

def controlPanel(request):
    return render(request, 'controlPanel/controlPanel.html')



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
