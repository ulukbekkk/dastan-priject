from django.shortcuts import render
from django.http import HttpResponse
from main.models import Category, Product


def get_main(request):
    products = Product.objects.all()
    print(locals())
    return render(request, 'product.html', locals())

def category(request):
    categories = Category.objects.all()
    return render(request, 'category.html', {'categories': categories})


