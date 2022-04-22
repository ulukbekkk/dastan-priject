from django.shortcuts import render
from django.http import HttpResponse


def get_main(request):
    return HttpResponse('<h1>МОЯ ТРЕТЬЯ РАБОТА</h1>')

def get_index(request):
    return render(request, 'index.html', {})
