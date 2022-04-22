from django.shortcuts import render
from django.http import HttpResponse


def get_main(request):
    return HttpResponse('<h1>ЧЕТВЕРТАЯ РАБОТА</h1>')


def get_index(request):
    return render(request, 'index.html', {})


def get_left_sidebar(request):
    return render(request, 'left-sidebar.html', {})


def get_no_sidebar(request):
    return render(request, 'no-side-bar.html', {})


def get_right_sidebar(request):
    return render(request, 'right-sidebar.html', {})
