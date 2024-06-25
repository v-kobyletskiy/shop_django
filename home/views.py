from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    context = {
        'title': 'Home - Главная',
        'content': 'Магазин мебели HOME',
    }
    return render(request, 'index.html', context)  # 'main/index.html'
    # return HttpResponse("<h1>Hello World</h1>")


def about(request):
    context = {
        'title': 'Home - О нас',
        'content': 'О нас',
        'text_on_page': 'Текст, чому магазин класний',
    }
    return render(request, 'about.html', context)
