from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_main, name='main'),
    #path('category/', views.category, name='category')
]