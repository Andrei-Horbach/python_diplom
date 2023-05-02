from django.contrib import admin
from .models import *


# Регистрация и настройка модели Author
@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    # Порядок вывода СТОЛБИКОВ (при отображении модели)
    list_display = ['__str__', 'last_name', 'first_name', 'img', 'sure_name', 'age', 'work_experience']


# Регистрация и настройка модели Genre
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'name']


# Регистрация и настройка модели Genre
@admin.register(Groups)
class GroupsAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'name']
