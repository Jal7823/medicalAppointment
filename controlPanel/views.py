from django.shortcuts import render

# Create your views here.

def controlPanel(request):
    return render(request, 'controlPanel/controlPanel.html')
