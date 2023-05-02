from django.shortcuts import render
from django.http import HttpResponse
from .models import *  # Импорт всех моделей


def index(request):
    categorys = Category.objects.all()
    teachers = Teacher.objects.all()
    context = {'categorys': categorys, 'teachers': teachers}
    return render(request, "index.html", context=context)
