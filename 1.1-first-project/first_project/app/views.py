from django.http import HttpResponse
from django.shortcuts import render, reverse
import datetime
import os

def home_view(request):
    template_name = 'app/home.html'
    # впишите правильные адреса страниц, используя
    # функцию `reverse`
    pages = {
        'Главная страница': reverse('home'),
        'Показать текущее время': reverse('time'),
        'Показать содержимое рабочей директории': reverse('workdir')
    }
    
    # context и параметры render менять не нужно
    # подбробнее о них мы поговорим на следующих лекциях
    context = {
        'pages': pages
    }
    return render(request, template_name, context)


def time_view(request):
    current_time = datetime.datetime.now().time()
    msg = f'Текущее время: {current_time}'
    context = {
        'time': msg
    }
    return render(request, 'app/time.html', context)


def workdir_view(request):
    template_name = 'app/workdir.html'
    dirs = list(os.listdir())
    print(dirs)

    # workdir = {num: dir for num, dir in dirs}
    # workdirs = {}
    # # for i in workdir.items():
    # #     workdirs[] =
    # #
    # #     print(': '.join(str(el) for el in i))
    context = {
        "workdirs": dirs,
    }
    print(dirs)
    return render(request, template_name, context)
