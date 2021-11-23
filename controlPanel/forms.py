from django import forms
from usersApp.models import Usuario


class CreateMedicForms(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ('')