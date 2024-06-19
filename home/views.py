from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    context = {
        'title': 'title abc',
        'content': 'content abc',
        'list': ['first', 'second', 'third'],
        'dict': {'first': 1},
        'bool': True,
    }
    return render(request, 'index.html', context)  # 'main/index.html'
    # return HttpResponse("<h1>Hello World</h1>")


def about(request):
    return HttpResponse("<h1>About</h1>")
