from django.db import models
from django.contrib.auth.models import User  # встроенная модель "Пользователи"


# 1. Модель Категории (Category) - Виды занятий
# Поля: name(категория)
class Category(models.Model):
    name = models.CharField(max_length=200,
                            help_text="Введите категорию занятия",
                            verbose_name="Категория занятия")

    # При просмотре всей модели из админки (поле которое будет отображаться)
    def __str__(self):
        return self.name

    # НАСТРОЙКИ перевода модели и сортировки объектов на главной таблице
    class Meta:
        verbose_name = "Предмет"  # Название модели в ед. Числе
        verbose_name_plural = "Предметы"  # Название модели во мн. Числе
        ordering = ["name"]  # Сортировка по полю


# 1. Модель Группы (Groups) - Возрастная группа преподавания
# Поля: name(группа)
class Groups(models.Model):
    name = models.CharField(max_length=200,
                            help_text="Введите возрастную группу",
                            verbose_name="Возрастная группа")

    # При просмотре всей модели из админки (поле которое будет отображаться)
    def __str__(self):
        return self.name

    # НАСТРОЙКИ перевода модели и сортировки объектов на главной таблице
    class Meta:
        verbose_name = "Возраст"  # Название модели в ед. Числе
        verbose_name_plural = "Возраста"  # Название модели во мн. Числе
        ordering = ["name"]  # Сортировка по полю


# 2. Модель Учителя (Teacher)
# Поля: first_name(Имя автора), last_name(Фамилия), sure_name(Отчество) subjects(предмет/дисциплина),age(возраст), work_experience(опыт работы)
class Teacher(models.Model):
    first_name = models.CharField(max_length=100, help_text="Введите имя преподавателя",
                                  verbose_name="Имя преподавателя")
    last_name = models.CharField(max_length=100, help_text="Введите фамилию преподавателя",
                                 verbose_name="Фамилия преподавателя")
    sure_name = models.CharField(max_length=100, help_text="Введите отчество преподавателя",
                                 verbose_name="Отчество преподавателя")
    subjects = models.ManyToManyField(Category, help_text="Выберите предмет занятий", verbose_name="Предмет занятий")
    age = models.IntegerField(null=True, help_text="Введите возраст преподавателя", verbose_name="Возраст")
    work_experience = models.IntegerField(null=True, help_text="Введите стаж работы", verbose_name="Стаж работы")
    img = models.ImageField(upload_to='media/images', null=True, help_text='150x150px', verbose_name="ссылка картинки")
    age_group = models.ManyToManyField(Groups, help_text="Введите группу преподавания", verbose_name="группа преподавания")

    # При просмотре всей модели из админки (поле которое будет отображаться)
    def __str__(self):
        return "{} {} {} {}".format(self.last_name, self.first_name, self.sure_name, self.age_group)

    # НАСТРОЙКИ перевода модели и сортировки объектов на главной таблице
    class Meta:
        verbose_name = "Преподаватель"  # Название модели в ед. числе род. падежа
        verbose_name_plural = "Преподаватели"  # Название модели во мн. числе
        ordering = ["last_name"]  # Сортировка по полю (если со знаком "-" то в обратном порядке)



