# Generated by Django 4.2 on 2023-05-02 16:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('v_kraskah', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='teacher',
            name='subjects',
            field=models.ManyToManyField(help_text='Выберите предмет занятий', to='v_kraskah.category', verbose_name='Предмет занятий'),
        ),
    ]
