from django.db import models
from django.core.validators import RegexValidator


# 1. Модель Категории (Category) - Виды занятий
# Поля: name(категория)
class Category(models.Model):
    name = models.CharField(max_length=200,
                            help_text="Введите категорию занятия",
                            verbose_name="Категория занятия")
    full_description = models.TextField(max_length=1000, help_text="Полный текст курса", verbose_name="полное описание",
                                        blank=True)
    short_description = models.CharField(max_length=200, help_text="Кратко опишите категорию",
                                         verbose_name="краткое описание", blank=True)
    img = models.ImageField(upload_to='media/images/category', null=True, help_text='150x150px',
                            verbose_name="ссылка картинки", blank=True)

    @property
    def photo_url(self):
        if self.img and hasattr(self.img, 'url'):
            return self.img.url

    # [ВНУТРЕННИЙ МЕТОД]. Метод возвращающий ссылку на категорию
    def get_absolute_url(self):
        return "/category/{}".format(self.pk)  # self.pk тоже самое что self.id

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
class Group(models.Model):
    name = models.CharField(max_length=200,
                            help_text="Введите название возрастной группы",
                            verbose_name="Название возрастной группы")
    ages = models.CharField(max_length=200,
                            help_text="Введите возрастную группу",
                            verbose_name="Возрастная группа", blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True)

    # При просмотре всей модели из админки (поле которое будет отображаться)
    def __str__(self):
        return '{}, {}'.format(self.name, self.ages)

    # НАСТРОЙКИ перевода модели и сортировки объектов на главной таблице
    class Meta:
        verbose_name = "Возраст"  # Название модели в ед. Числе
        verbose_name_plural = "Возрасты"  # Название модели во мн. Числе
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
    img = models.ImageField(upload_to='media/images/teachers', null=True, help_text='150x150px', verbose_name="ссылка картинки")
    age_group = models.ManyToManyField(Group, help_text="Введите группу преподавания",
                                       verbose_name="группа преподавания")

    def get_age_group(self):
        lst_age_group = []
        for gruop in self.age_group.all():
            lst_age_group.append(gruop.name)
        return ", ".join(lst_age_group)

    def get_subject(self):
        lst_subject = []
        for subject in self.subjects.all():
            lst_subject.append(subject.name)
        return ", ".join(lst_subject)

    def get_absolute_url(self):
        return "/price"

    def get_absolute_url_subject(self):
        return "/categorys"

    @property
    def photo_url(self):
        if self.img and hasattr(self.img, 'url'):
            return self.img.url

    # При просмотре всей модели из админки (поле которое будет отображаться)
    def __str__(self):
        return "{} {} {}".format(self.last_name, self.first_name, self.sure_name)

    # НАСТРОЙКИ перевода модели и сортировки объектов на главной таблице
    class Meta:
        verbose_name = "Преподаватель"  # Название модели в ед. числе род. падежа
        verbose_name_plural = "Преподаватели"  # Название модели во мн. числе
        ordering = ["last_name"]  # Сортировка по полю (если со знаком "-" то в обратном порядке)


class UserCallBack(models.Model):
    name = models.CharField(max_length=100, help_text="Имя", verbose_name="Имя клиента")
    phoneNumberRegex = RegexValidator(regex=r"^\+?1?\d{8,15}$")
    phoneNumber = models.CharField(validators=[phoneNumberRegex], max_length=16, unique=True, help_text="Номер телефона", verbose_name="Номер телефона клиента")

    def __str__(self):
        return "{}, {}".format(self.name, self.phoneNumber)

    class Meta:
        verbose_name = "Пользователь (регистрация на курс)"  # Название модели в ед. числе род. падежа
        verbose_name_plural = "Пользователи (регистрация на курс)"  # Название модели во мн. числе