from django import forms
from Usuarios.models import Usuario


class CreateMedicForms(forms.ModelForm):
    specialty = Usuario.objects.all()
    class Meta:
        model = Usuario
        fields = ('__all__')
        widgets = {
            'isDoctors':forms.
        }