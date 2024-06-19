from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.http import JsonResponse
from django.template import loader
from .forms import *
import random

# Create your views here.
def lesson1view(request):
    template = loader.get_template("../templates/index.html")
    dictionary1 = [
        ('Быть', 'Be', 'Was/were', 'Been') ,
        ('Бить', 'Beat', 'Beat', 'Beaten') ,
        ('Становиться', 'Become', 'Became', 'Become') ,
        ('Начинать', 'Begin', 'Began', 'Begun') ,
        ('Гнуть', 'Bend', 'Bent', 'Bent') ,
        
        ('Держать', 'Bet', 'Bet', 'Bet') ,
        ('Кусать', 'Bite', 'Bit', 'Bitten') ,
        ('Дуть', 'Blow', 'Blew', 'Blown') ,
        ('Ломать', 'Break', 'Broke', 'Broken') ,
        ('Приносить', 'Bring', 'Brought', 'Brought') ,
        
        ('Строить', 'Build', 'Built', 'Built') ,
        ('Покупать', 'Buy', 'Bought', 'Bought') ,
        ('Ловить', 'Catch', 'Caught', 'Caught') ,
        ('Выбирать', 'Choose', 'Chose', 'Chosen') ,
        ('Приходить', 'Come', 'Came', 'Come') ,
        
        ('Стоить', 'Cost', 'Cost', 'Cost') ,
        ('Резать', 'Cut', 'Cut', 'Cut') ,
        ('Иметь', 'Deal', 'Dealt', 'Dealt') ,
        ('Копать', 'Dig', 'Dug', 'Dug') ,
        ('Делать', 'Do', 'Did', 'Done') ,
        
        ('Рисовать', 'Draw', 'Drew', 'Drawn') ,
        ('Пить', 'Drink', 'Drank', 'Drunk') ,
        ('Ездить', 'Drive', 'Drove', 'Driven') ,
        ('Есть', 'Eat', 'Ate', 'Eaten') ,
        ('Падать', 'Fall', 'Fell', 'Fallen') ,
        
        ('Кормить', 'Feed', 'Fed', 'Fed') ,
        ('Чувствовать', 'Feel', 'Felt', 'Felt') ,
        ('Драться', 'Fight', 'Fought', 'Fought') ,
        ('Находить', 'Find', 'Found', 'Found') ,
        ('Летать', 'Fly', 'Flew', 'Flown') ,
        
        ('Забывать', 'Forget', 'Forgot', 'Forgotten') ,
        ('Прощать', 'Forgive', 'Forgave', 'Forgiven') ,
        ('Замерзать', 'Freeze', 'Froze', 'Frozen') ,
        ('Получать', 'Get', 'Got', 'Got') ,
        ('Дать', 'Give', 'Gave', 'Given') ,
        
        ('Идти', 'Go', 'Went', 'Gone') ,
        ('Расти', 'Grow', 'Grew', 'Grown') ,
        ('Вешать', 'Hang', 'Hung', 'Hung') ,
        ('Иметь', 'Have', 'Had', 'Had') ,
        ('Слышать', 'Hear', 'Heard', 'Heard') ,
        
        ('Прятать', 'Hide', 'Hid', 'Hidden') ,
        ('Ударять', 'Hit', 'Hit', 'Hit') ,
        ('Держать', 'Hold', 'Held', 'Held') ,
        ('Ранить', 'Hurt', 'Hurt', 'Hurt') ,
        ('Хранить', 'Keep', 'Kept', 'Kept') ,
        
        ('Знать', 'Know', 'Knew', 'Known') ,
        ('Класть', 'Lay', 'Laid', 'Laid') ,
        ('Вести', 'Lead', 'Led', 'Led') ,
        ('Покидать', 'Leave', 'Left', 'Left') ,
        ('Одалживать', 'Lend', 'Lent', 'Lent') ,
        
        ('Позволять', 'Let', 'Let', 'Let') ,
        ('Лежать', 'Lie', 'Lay', 'Lain') ,
        ('Зажигать', 'Light', 'Lit', 'Lit') ,
        ('Терять', 'Lose', 'Lost', 'Lost') ,
        ('Делать', 'Make', 'Made', 'Made') ,
        
        ('Значить', 'Mean', 'Meant', 'Meant') ,
        ('Встречать', 'Meet', 'Met', 'Met') ,
        ('Платить', 'Pay', 'Paid', 'Paid') ,
        ('Ставить', 'Put', 'Put', 'Put') ,
        ('Читать', 'Read', 'Read', 'Read') ,
        
        ('Ехать', 'Ride', 'Rode', 'Ridden') ,
        ('Звенеть', 'Ring', 'Rang', 'Rung') ,   
        ('Восходить', 'Rise', 'Rose', 'Risen') ,
        ('Бежать', 'Run', 'Ran', 'Run') ,
        ('Говорить', 'Say', 'Said', 'Said') ,
        
        ('Видеть', 'See', 'Saw', 'Seen') ,
        ('Искать', 'Seek', 'Sought', 'Sought') ,
        ('Продавать', 'Sell', 'Sold', 'Sold') ,
        ('Посылать', 'Send', 'Sent', 'Sent') ,
        ('Устанавливать', 'Set', 'Set', 'Set') ,
        
        ('Трясти', 'Shake', 'Shook', 'Shaken') ,
        ('Светить', 'Shine', 'Shone', 'Shone') ,
        ('Стрелять', 'Shoot', 'Shot', 'Shot') ,
        ('Показывать', 'Show', 'Showed', 'Shown') ,
        ('Закрывать', 'Shut', 'Shut', 'Shut') ,
        
        ('Петь', 'Sing', 'Sang', 'Sung') ,
        ('Тонуть', 'Sink', 'Sank', 'Sunk') ,
        ('Сидеть', 'Sit', 'Sat', 'Sat') ,
        ('Спать', 'Sleep', 'Slept', 'Slept') ,
        ('Говорить', 'Speak', 'Spoke', 'Spoken') ,
        
        ('Тратить', 'Spend', 'Spent', 'Spent') ,
        ('Стоять', 'Stand', 'Stood', 'Stood') ,
        ('Воровать', 'Steal', 'Stole', 'Stolen') ,
        ('Втыкать', 'Stick', 'Stuck', 'Stuck') ,
        ('Клясться', 'Swear', 'Swore', 'Sworn') ,
        
        ('Мести', 'Sweep', 'Swept', 'Swept') ,
        ('Плавать', 'Swim', 'Swam', 'Swum') ,
        ('Качаться', 'Swing', 'Swung', 'Swung') ,
        ('Брать', 'Take', 'Took', 'Taken') ,
        ('Учить', 'Teach', 'Taught', 'Taught') ,
        
        ('Рвать', 'Tear', 'Tore', 'Torn') ,
        ('Рассказывать', 'Tell', 'Told', 'Told') ,
        ('Думать', 'Think', 'Thought', 'Thought') ,
        ('Бросать', 'Throw', 'Threw', 'Thrown') ,
        ('Понимать', 'Understand', 'Understood', 'Understood') ,
        
        ('Просыпаться', 'Wake', 'Woke', 'Woken') ,
        ('Носить', 'Wear', 'Wore', 'Worn') ,
        ('Победить', 'Win', 'Won', 'Won') ,
        ('Писать', 'Write', 'Wrote', 'Written') ,
    ]
    dictset = random.choice(dictionary1)
    initial_data = {'target': dictset[0]}
    form = AnswerForm(initial=initial_data)
    if request.method != "POST":
        initial_data = {'target': dictset[0]}
        form = AnswerForm(initial=initial_data)
        content = {"form": form,
#               "result": result, 
               "word" : dictset[0], 
               "realanswer1": dictset[1], 
               "realanswer2": dictset[2], 
               "realanswer3": dictset[3]
               }
#     return HttpResponse(template.render(context, request))
        return render(request, 'lesson-1.html', context=content)

    else:
        form = AnswerForm(request.POST)
        if form.is_valid():
            target = form.cleaned_data['target']
            dictset = next(item for item in dictionary1 if item[0] == target)
            word1 = form.cleaned_data['infinitive']
            word2 = form.cleaned_data['past_simple']
            word3 = form.cleaned_data['past_participle']
            content = {"form": form,
#               "result": result, 
               "word" : dictset[0], 
               "realanswer1": dictset[1], 
               "realanswer2": dictset[2], 
               "realanswer3": dictset[3],
               "useranswer1": word1,
               "useranswer2": word2,
               "useranswer3": word3,    
            }
            return render(request, 'lesson-1_answer.html', context=content)

def lesson2view(request):
    template = loader.get_template("../templates/index.html")
    dictionary2 = [("Log in", "Входить в систему"),
           ("Set up", "Устанавливать"),
           ("Log out","Выходить из системы"),
           ("Turn on","Включать"),
           ("Turn off","Выключать"),
           
           ("Plug in","Подключать"),
           ("Shut down","Выключать"),
           ("Boot up","Загружаться"),
           ("Back up","Создать резерв. копию"),
           ("Break down","Ломаться"),
           
           ("Check in","Зарегистрироваться"),
           ("Check out","Выписываться"),
           ("Look up","Искать"),
           ("Call off","Отменять"),
           ("Cut off","Прерывать"),
    ]
    para = random.choice(dictionary2)
    # выбираем пару случайным образом
    content = {"eng" : para[0], "ru": para[1]}
#     return HttpResponse(template.render(context, request))
    return render(request, 'lesson-2.html', context=content)

def lesson4view(request):
    template = loader.get_template("../templates/index.html")
    dictionary4en = [
        'Accept',
        'Allow',
        'Ask',
        'Believe',
        'Borrow',
        'Break',
        'Bring',
        'Buy',
        'Call',
        'Choose',
        'Come',
        'Cook',
        'Create',
        'Dance',
        'Decide',
        'Describe',
        'Eat',
        'Enjoy',
        'Explain',
        'Feel',
        'Find',
        'Forget',
        'Get',
        'Give',
        'Go',
        'Hear',
        'Help',
        'Keep',
        'Know',
        'Learn',
        'Leave',
        'Like',
        'Listen',
        'Live',
        'Look',
        'Love',
        'Make',
        'Need',
        'Open',
        'Play',
        'Put',
        'Read',
        'Remember',
        'Run',
        'Say',
        'See',
        'Sell',
        'Send',
        'Show',
        'Sit',
        'Sleep',
        'Speak',
        'Spend',
        'Stand',
        'Start',
        'Stop',
        'Study',
        'Take',
        'Talk',
        'Teach',
        'Tell',
        'Think',
        'Travel',
        'Try',
        'Understand',
        'Use',
        'Wait',
        'Walk',
        'Want',
        'Watch',
        'Work',
        'Write',
    ]
    dictionary4ru = [
        'Принимать',
        'Разрешать',
        'Спрашивать',
        'Верить',
        'Брать',
        'Ломать',
        'Приносить',
        'Покупать',
        'Звать',
        'Выбирать',
        'Приходить',
        'Готовить',
        'Создавать',
        'Танцевать',
        'Решать',
        'Описывать',
        'Есть',
        'Наслаждаться',
        'Объяснять',
        'Чувствовать',
        'Находить',
        'Забывать',
        'Получать',
        'Давать',
        'Идти',
        'Слышать',
        'Помогать',
        'Держать',
        'Знать',
        'Учить(ся)',
        'Покидать',
        'Нравиться',
        'Слушать',
        'Жить',
        'Смотреть',
        'Любить',
        'Делать',
        'Нуждаться',
        'Открывать',
        'Играть',
        'Класть',
        'Читать',
        'Помнить',
        'Бежать',
        'Говорить',
        'Видеть',
        'Продавать',
        'Отправлять',
        'Показывать',
        'Сидеть',
        'Спать',
        'Говорить',
        'Тратить',
        'Стоять',
        'Начинать',
        'Останавливать',
        'Учить(ся)',
        'Брать',
        'Разговаривать',
        'Учить',
        'Рассказывать',
        'Думать',
        'Путешествовать',
        'Пробовать',
        'Понимать',
        'Использовать',
        'Ждать',
        'Ходить',
        'Хотеть',
        'Смотреть',
        'Работать',
        'Писать',
    ]
    rightwordptr = random.randint(0, 71)
    rightbuttonptr = random.randint(1, 4)

    word = ['','','','','']
    word[0] = dictionary4en[rightwordptr]
    word[1] = dictionary4ru[random.randint(0, 71)]
    word[2] = dictionary4ru[random.randint(0, 71)]
    word[3] = dictionary4ru[random.randint(0, 71)]
    word[4] = dictionary4ru[random.randint(0, 71)]
    word[rightbuttonptr] = dictionary4ru[rightwordptr]

    if request.method != "POST":
        content = {
#               "result": result, 
               "word_in_eng" : word[0], 
               "option1": word[1], 
               "option2": word[2], 
               "option3": word[3],
               "option4": word[4],
            }
#     return HttpResponse(template.render(context, request))
        return render(request, 'lesson-4.html', context=content)

    else:
        button_value = request.POST.get('button')
        print(button_value)
        content = { "value": button_value, 
#           "result": result, 
           "word_in_eng" : word[0], 
           "option1": word[1], 
           "option2": word[2], 
           "option3": word[3],
           "option4": word[4],
        }
        return render(request, 'lesson-4_answer.html', context=content)