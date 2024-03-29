from django import forms
from .models import Appointment
from django.contrib.auth.models import User
from tempus_dominus.widgets import DatePicker, TimePicker, DateTimePicker
from usersApp.models import Usuario


class formsAppointment(forms.ModelForm):
    date = forms.DateField(
        label='Fecha',
        widget=forms.DateInput(attrs={'class': 'datepicker', 'autocomplete': 'off'}),
    )
    class Meta:
        model = Appointment
        fields = '__all__'
        exclude = ('user',)
        labels = {
            'specialty':'Especialidad',
            'date':'Fecha',
            'branchOffices':'Seleccion la oficina'

        }
