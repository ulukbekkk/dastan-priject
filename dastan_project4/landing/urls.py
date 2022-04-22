from django.urls import path
from . import views


urlpatterns = [
    path('',views.get_main, name='main'),
    path('index/', views.get_index),
    path('left-sidebar/', views.get_left_sidebar),
    path('no-sidebar/', views.get_no_sidebar),
    path('right-sidebar/', views.get_right_sidebar)
]