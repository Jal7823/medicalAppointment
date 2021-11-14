from django import forms
from .models import Appointment
from django.contrib.auth.models import User
from usersApp.models import Usuario





class formsAppointment(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = '__all__'
        widgets = {
            'date':forms.DateInput(),
        }

