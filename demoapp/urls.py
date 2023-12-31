from django.urls import path
from . import views

urlpatterns = [
    path('home', views.home, name="home"),
    path('about', views.about, name="about"),
    path('menu', views.menu, name="menu"),
    path('book', views.book, name="book"),
    path('', views.index, name='index'),
    path('booking/', views.form_view),
]