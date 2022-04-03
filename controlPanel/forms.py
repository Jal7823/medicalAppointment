from django import forms
from multiselectfield import MultiSelectField
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

class CreatePatient(forms.ModelForm):
    class Meta:
        model = Usuario
        fields =['username','email','password','lastName','dni','direc','loc','pcia','tlf','sick','doctors','patology']
        widgets = {
            'sick':forms.CheckboxInput(),
            'pcia':forms.Select(attrs={'class':'form-control'}),
            'password':forms.PasswordInput(),
            'doctors':forms.CheckboxSelectMultiple(),
            'patology':forms.CheckboxSelectMultiple()
        }


class UpdatePatient(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ('name','lastName','dni','doctors','patology','sick','history','image')
        widgets = {
            'doctors':forms.CheckboxSelectMultiple(),
            'patology':forms.CheckboxSelectMultiple(),
        }
