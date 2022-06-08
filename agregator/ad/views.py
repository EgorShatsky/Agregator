from django.shortcuts import render
from django.http import HttpResponse
from . models import *

menu = [{'title': 'Объявления', 'url_name': 'announcement'},
        {'title': 'О сайте', 'url_name': 'about'},
        {'title': 'Войти', 'url_name': 'login'},
        {'title': 'Разместить объявление', 'url_name': 'add_page'}
]


def index(request):
    return render(request, 'ad/index.html', {'menu': menu, 'title': 'Главная страница'})


def announcement(request):
    posts = Announcement.objects.all()
    cats = Category.objects.all()

    context = {
        'posts': posts,
        'menu': menu,
        'cats': cats,
        'title': 'Активные объявления',
        'cat_selected': 0,

    }
    return render(request, 'ad/announcement.html', context=context)


def about(request):
    return render(request, 'ad/about.html', {'menu': menu, 'title': 'О сайте'})


def login(request):
    return render(request, 'ad/login.html', {'menu': menu, 'title': 'Вход в личный кабинет'})


def add_page(request):
    return render(request, 'ad/add_page.html', {'menu': menu, 'title': 'Добавить объявление'})


def show_category(request, cat_id):
    posts = Announcement.objects.filter(cat_id=cat_id)
    cats = Category.objects.all()

    context = {
        'posts': posts,
        'menu': menu,
        'cats': cats,
        'title': f'Активные объявления {cats[cat_id-1]}',
        'cat_selected': cat_id,

    }
    return render(request, 'ad/index.html', context=context)


