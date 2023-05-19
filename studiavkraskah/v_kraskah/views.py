from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from django.views import generic
from .forms import Course_registration


# Главная страница
def index(request):
    context = {}
    return render(request, "index.html", context=context)


# Метод возвращающий шаблон "templates/call_back.html"
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


# Метод возвращающий шаблон "templates/answer.html"
def answer(request):
    return render(request, 'answer.html')


# Возвращает все Группы. (Автоматически генерируется при помощи DetailView)
# Шаблон "templates/v-kraskah/group_list.html"
class PriceListView(generic.ListView):
    model = Group


# Возвращает все категории.
# Шаблон "templates/v-kraskah/category_list.html"
class CategoryListView(generic.ListView):
    model = Category


# Возвращает конкретную категорию.
# Шаблон "templates/v-kraskah/category_detail.html"
class CategoryDetailView(generic.DetailView):
    model = Category


# Возвращает всех преподавателей.
# Шаблон "templates/v-kraskah/teacher_list.html"
class TeacherListView(generic.ListView):
    model = Teacher
    paginate_by = 3


# Метод "Наши правила".
# Шаблон "templates/our_rules.html"
def our_rules(request):
    return render(request, "our_rules.html")


# Метод "Контакты".
# Шаблон "templates/contacts.html"
def contacts(request):
    return render(request, "contacts.html")
