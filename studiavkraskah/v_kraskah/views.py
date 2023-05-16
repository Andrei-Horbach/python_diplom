from typing import Dict, Any

from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *  # Импорт всех моделей
from django.views import generic  # Нужен для автоматического чтения
from .forms import Course_registration


def index(request):
    context = {}
    return render(request, "index.html", context=context)


def call_back(request):
    error = ''
    if request.method == "POST":
        form = Course_registration(request.POST)
        if form.is_valid():
            form.save()
            return redirect('answer')
        else:
            error = 'Неверные данные, попробуйте заполнить снова!'
    form = Course_registration()

    data = {'form': form,
            'error': error}
    return render(request, 'call_back.html', data)


def answer(request):
    return render(request, 'answer.html')


class PriceListView(generic.ListView):
    model = Group


class CategoryListView(generic.ListView):
    model = Category


# Возвращает конкретную книгу. (Автоматически генерируется при помощи DetailView)
# Шаблон "templates/catalog/book_detail.html"
# Переменная (входная): "int:pk"
# Переменная (шаблона/ключ): "book"
class CategoryDetailView(generic.DetailView):
    model = Category


class TeacherListView(generic.ListView):
    model = Teacher
    paginate_by = 3


def our_rules(request):
    return render(request, "our_rules.html")


def contacts(request):
    return render(request, "contacts.html")
