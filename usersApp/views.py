import random
from django.http import HttpResponseRedirect
from django.db.models import Q
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


def register(request):
    data = {
        'form': CustomUserCreationForm()
    }

    if request.method == 'POST':
        form = CustomUserCreationForm(data=request.POST)
        if form.is_valid():
            form.save()

            user = authenticate(
                username=form.cleaned_data['username'], password=form.cleaned_data['password1'])
            login(request, user)
            return redirect(to='login')

        data['form'] = form
        messages.error(request, 'algo fallo en la suscripcion')
    return render(request, 'usersApp/registration.html', data)


class LogoutView(LogoutView):
    pass


def register_form(request):

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
    user = Usuario.objects.get(Q(id=id))
    numberCard = random.randint(0, 9999_9999_9999_9999)
    traspast = str(numberCard)

    user.nrMembership=traspast
    user.save()
    context = {
        'separator': traspast,
    }

    return HttpResponseRedirect(request.META.get('HTTP_REFERER', f"DetailUserProfile/{id}"))
