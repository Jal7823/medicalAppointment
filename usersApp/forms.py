from django import forms
from .models import Usuario
from django.contrib.auth.forms import UserCreationForm



class CustomUserCreationForm(forms.ModelForm):

    password1 = forms.CharField(label='Contraseña', widget= forms.PasswordInput(
        attrs = {
            'class':'form-control',
            'placeholder':'Ingrese su contraseña',
            'id':'password1',
            'required':'required'

        }
    ))

    password2 = forms.CharField(label='Contraseña', widget= forms.PasswordInput(
        attrs = {
            'class':'form-control',
            'placeholder':'Ingrese nuevamente su contraseña',
            'id':'password2',
            'required':'required'

        }
    ))


    def clean_password2(self):
        '''
        
        validamos que la contrasena igresada en ambos campos sean iguales 

        '''


        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if password1 != password2:
            raise forms.ValidationError('contraseñas no coinciden')
        return password2

    class Meta:
        model = Usuario
        fields = ('username','email','password1','password2','name','lastName','dni','direc','loc','pcia','tlf')

    def save(self,commit=True):
        '''

        redefinimos el metodo save        

        '''
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        return user




class UpdateProfileUser(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ('name','lastName','image','dni','direc','loc','pcia','tlf')
        labels = {
            'name':'Nombre',
            'lastName':'Apellido',
            'direc':'Direccion',
            'loc':'Localidad',
            'pcia':'Provincia',
            'tlf':'Telefono',
        }

