from django.contrib import admin
from .models import *


# Регистрация и настройка модели Author
@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    # Порядок вывода СТОЛБИКОВ (при отображении модели)
    list_display = ['__str__', 'last_name', 'first_name']


# Регистрация и настройка модели Genre
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'name']


@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'name']


@admin.register(UserCallBack)
class UserCallBackAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'name']
