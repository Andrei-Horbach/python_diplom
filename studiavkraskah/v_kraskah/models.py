from django.db import models
from django.core.validators import RegexValidator


# Модель Категории (Category) - Предмет занятий
# Поля: name(категория), full_description(полное описание при открытии страницы), short_description(краткое превью
# на общей странице), img(картинка)
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

    # Метод для отображения изображений из модели
    @property
    def photo_url(self):
        if self.img and hasattr(self.img, 'url'):
            return self.img.url

    # Метод возвращающий ссылку на категорию
    def get_absolute_url(self):
        return "/category/{}".format(self.pk)  # self.pk тоже самое что self.id

    # При просмотре всей модели из админки (поле которое будет отображаться)
    def __str__(self):
        return self.name

    # НАСТРОЙКИ перевода модели и сортировки объектов на главной таблице
    class Meta:
        verbose_name = "Предмет"
        verbose_name_plural = "Предметы"
        ordering = ["name"]


# Модель Группы (Groups) - Возрастная группа преподавания
# Поля: name(группа), ages(возраст), price(стоимость)
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
        verbose_name = "Возраст"
        verbose_name_plural = "Возрасты"
        ordering = ["name"]


# Модель Учителя (Teacher)
# Поля: first_name(Имя автора), last_name(Фамилия), sure_name(Отчество) subjects(предмет/дисциплина),age(возраст),
# work_experience(опыт работы), img(фотография), age_group(какую группу преподает)
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
    img = models.ImageField(upload_to='media/images/teachers', null=True, help_text='150x150px',
                            verbose_name="ссылка картинки")
    age_group = models.ManyToManyField(Group, help_text="Введите группу преподавания",
                                       verbose_name="группа преподавания")

    # Метод для передачи в шаблон Group.name
    def get_age_group(self):
        lst_age_group = []
        for gruop in self.age_group.all():
            lst_age_group.append(gruop.name)
        return ", ".join(lst_age_group)

    # Метод для передачи в шаблон subject.name
    def get_subject(self):
        lst_subject = []
        for subject in self.subjects.all():
            lst_subject.append(subject.name)
        return ", ".join(lst_subject)

    # Метод возвращающий ссылку на прайс
    def get_absolute_url(self):
        return "/price"

    # Метод возвращающий ссылку на категории
    def get_absolute_url_subject(self):
        return "/categorys"

    # Метод для отображения изображений из модели
    @property
    def photo_url(self):
        if self.img and hasattr(self.img, 'url'):
            return self.img.url

    def __str__(self):
        return "{} {} {}".format(self.last_name, self.first_name, self.sure_name)

    class Meta:
        verbose_name = "Преподаватель"
        verbose_name_plural = "Преподаватели"
        ordering = ["last_name"]


# Модель Пользователи на обратный звонок (UserCallBack), наполняется из формы Course_registration(ModelForm)
# Поля: name(Имя пользователя), phoneNumberRegex(внутренне поле), phoneNumber(номер телефона)
class UserCallBack(models.Model):
    name = models.CharField(max_length=100, help_text="Имя", verbose_name="Имя клиента")
    phoneNumberRegex = RegexValidator(regex=r"^\+?1?\d{8,15}$")
    phoneNumber = models.CharField(validators=[phoneNumberRegex], max_length=16, unique=True,
                                   help_text="Номер телефона", verbose_name="Номер телефона клиента")

    def __str__(self):
        return "{}, {}".format(self.name, self.phoneNumber)

    class Meta:
        verbose_name = "Пользователь (регистрация на курс)"
        verbose_name_plural = "Пользователи (регистрация на курс)"
