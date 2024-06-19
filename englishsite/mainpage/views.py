from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import CustomUserCreationForm

# Create your views here.
def mainview(request):  
    template = loader.get_template("main.html")
    context = {}
    # return HttpResponse(template.render(context, request))
    return render(request, 'main.html')

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')  # Перенаправление на домашнюю страницу после успешной регистрации
    else:
        form = CustomUserCreationForm()
    return render(request, 'index.html', {'form': form})
