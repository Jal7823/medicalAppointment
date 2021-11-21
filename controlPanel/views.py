from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from appointment.models import Appointment
from usersApp.models import Usuario

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
