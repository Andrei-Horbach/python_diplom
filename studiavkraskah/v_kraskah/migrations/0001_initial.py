# Generated by Django 4.2 on 2023-05-01 13:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Введите категорию занятия', max_length=200, verbose_name='Категория занятия')),
            ],
            options={
                'verbose_name': 'Предмет',
                'verbose_name_plural': 'Предметы',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(help_text='Введите имя преподавателя', max_length=100, verbose_name='Имя преподавателя')),
                ('last_name', models.CharField(help_text='Введите фамилию преподавателя', max_length=100, verbose_name='Фамилия преподавателя')),
                ('sure_name', models.CharField(help_text='Введите отчество преподавателя', max_length=100, verbose_name='Отчество преподавателя')),
                ('age', models.IntegerField(help_text='Введите возраст преподавателя', null=True, verbose_name='Возраст')),
                ('work_experience', models.IntegerField(help_text='Введите стаж работы', null=True, verbose_name='Стаж работы')),
            ],
            options={
                'verbose_name': 'Преподаватель',
                'verbose_name_plural': 'Преподаватели',
                'ordering': ['last_name'],
            },
        ),
    ]
