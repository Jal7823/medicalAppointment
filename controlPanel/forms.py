from django import forms
from usersApp.models import Usuario


class CreateMedicForms(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ('username','name','lastName','password')
        labels = {
            'lastName':'Apellido',
        }
        widgets = {
            'isDoctors':forms.TextInput(attrs={'default':True}),
            'password':forms.PasswordInput(),
        }


class UpdatePatient(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ('name','lastName','dni','doctors','patology','sick','history','image')
        widgets = {
            'doctors':forms.CheckboxSelectMultiple(),
            'patology':forms.CheckboxSelectMultiple(),
        }
