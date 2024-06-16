from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.
def theoryview(request):
    template = loader.get_template("../templates/index.html")
    context = {}
    return HttpResponse(template.render(context, request))