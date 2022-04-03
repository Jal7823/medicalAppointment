import random
import datetime
from datetime import timedelta
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import (CreateView, DeleteView, DetailView, ListView,
                                  UpdateView)

from .forms import CustomUserCreationForm, UpdateProfileUser
from .models import Usuario


class LoginFromView(LoginView):
    template_name = 'registration/login.html'

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect(to='index')

        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Inicio de sesion'
        return context


def registro(request):
    data = {
        'form': CustomUserCreationForm()

    }

    if request.method == 'POST':
        formulario = CustomUserCreationForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()

            user = authenticate(
                username=formulario.cleaned_data['username'], password=formulario.cleaned_data['password1'])
            login(request, user)
            return redirect(to='login')

        data['form'] = formulario
        messages.error(request, 'algo fallo en la suscripcion')
    return render(request, 'usersApp/registration.html', data)


class LogoutView(LogoutView):
    pass


def formulario(request):

    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = CustomUserCreationForm()

    return render(request, 'registration.html', {'form': form})


class UserProfile(UpdateView):
    model = Usuario
    form_class = UpdateProfileUser
    template_name = 'usersApp/userProfile.html'
    success_url = reverse_lazy('index')


class DetailUserProfile(DeleteView):
    model = Usuario
    template_name = 'usersApp/userDetailProfile.html'


def createNumberMembership(request, id):
    numberCard = random.randint(0, 9999_9999_9999_9999)
    traspast = str(numberCard)
    separator = '{} {} {} {}'.format(
        traspast[:4], traspast[4:8], traspast[8:12], traspast[12:])
    user = Usuario.objects.filter(id=id)
    if user.nrMembership == '':
        message = 'Suscripcion creada con exito'

        user.update(nrMembership=numberCard)
    else:
        message = 'ya usted posee tarjeta de suscripcion'
        return message

    context = {
        'message': message,
        'separator': separator,
    }

    return render(request, 'usersApp/userDetailProfile.html', context)
