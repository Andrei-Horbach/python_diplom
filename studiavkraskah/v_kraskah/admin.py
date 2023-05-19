from django.contrib import admin
from .models import *


# Регистрация и настройка модели Teacher
@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    # Порядок вывода СТОЛБИКОВ (при отображении модели)
    list_display = ['__str__', 'last_name', 'first_name']


# Регистрация и настройка модели Category
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'name']


# Регистрация и настройка модели Group
@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'name']


# Регистрация и настройка модели UserCallBackAdmin
@admin.register(UserCallBack)
class UserCallBackAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'name']
