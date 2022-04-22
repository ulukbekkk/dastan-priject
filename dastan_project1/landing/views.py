from django.http import HttpResponse
from django.shortcuts import render


def get_main(request):
    return HttpResponse('<h1>ПРИВЕТ</h1>')


def get_index(request):
    return render(request, 'index.html', {})


