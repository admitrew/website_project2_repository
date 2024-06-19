from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.
def theory1view(request):
    template = loader.get_template("theory-1.html")
    return render(request, 'theory-1.html')