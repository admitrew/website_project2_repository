from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
import random

# Create your views here.
def lesson1view(request):
    template = loader.get_template("../templates/index.html")
    dictionary = [("Log in", "Входить в систему"),
           ("Set up", "Устанавливать"),
           ("Log out","Выходить (из системы)"),
           ("Turn on","Включать"),
           ("Turn off","Выключать"),
           
           ("Plug in","Подключать"),
           ("Shut down","Выключать"),
           ("Boot up","Загружать (компьютер)"),
           ("Back up","Создавать резерв. копию"),
           ("Break down","Ломаться"),
           
           ("Check in","Зарегистрироваться"),
           ("Check out","Выписываться"),
           ("Look up","Искать"),
           ("Call off","Отменять"),
           ("Cut off","Прерывать"),
    ]
    para = random.choice(dictionary)
    # выбираем пару случайным образом
    content = {"eng" : para[0], "ru": para[1]}
#     return HttpResponse(template.render(context, request))
    return render(request, 'lesson-1.html', context=content)

def lesson2view(request):
    template = loader.get_template("../templates/index.html")
    dictionary = [("Log in", "Входить в систему"),
           ("Set up", "Устанавливать"),
           ("Log out","Выходить (из системы)"),
           ("Turn on","Включать"),
           ("Turn off","Выключать"),
           
           ("Plug in","Подключать"),
           ("Shut down","Выключать"),
           ("Boot up","Загружать (компьютер)"),
           ("Back up","Создавать резерв. копию"),
           ("Break down","Ломаться"),
           
           ("Check in","Зарегистрироваться"),
           ("Check out","Выписываться"),
           ("Look up","Искать"),
           ("Call off","Отменять"),
           ("Cut off","Прерывать"),
    ]
    para = random.choice(dictionary)
    # выбираем пару случайным образом
    content = {"eng" : para[0], "ru": para[1]}
#     return HttpResponse(template.render(context, request))
    return render(request, 'lesson-2.html', context=content)