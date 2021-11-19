from django.contrib.auth.views import LoginView,LogoutView
from django.shortcuts import render,redirect
from .forms import CustomUserCreationForm


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
        'form':CustomUserCreationForm()
        
    }

    if request.method =='POST':
        formulario = CustomUserCreationForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()

            user = authenticate(username=formulario.cleaned_data['username'],password=formulario.cleaned_data['password1'])
            login(request,user)
            return redirect(to='login')


        data ['form'] = formulario 
        messages.error(request,'algo fallo en la suscripcion')
    return render(request,'usersApp/registration.html',data)

class LogoutView(LogoutView):
    pass

def formulario(request):
    
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect ('index')
    else:
        form = CustomUserCreationForm()

    return render(request,'registration.html',{'form':form})
