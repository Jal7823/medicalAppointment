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