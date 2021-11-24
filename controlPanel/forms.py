from django import forms
from doctors.models import Doctor


class CreateMedicForms(forms.ModelForm):
    specialty = Doctor.objects.all()
    class Meta:
        model = Doctor
        fields = ('__all__')
        widgets = {
            'specialty':forms.Select(attrs={
                                            'class':'form-select',
                                            'aria-label':'Default select example'
                                            }),
}