# Generated by Django 4.1.5 on 2023-05-08 12:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('v_kraskah', '0005_teacher_age_group'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='short_description',
            field=models.CharField(blank=True, help_text='Кратко опишите категорию', max_length=200, verbose_name='краткое описание'),
        ),
    ]
