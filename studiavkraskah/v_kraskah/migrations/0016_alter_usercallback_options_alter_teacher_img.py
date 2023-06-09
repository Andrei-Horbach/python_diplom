# Generated by Django 4.1.5 on 2023-05-15 11:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('v_kraskah', '0015_alter_usercallback_phonenumber'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='usercallback',
            options={'verbose_name': 'Пользователь (регистрация на курс)', 'verbose_name_plural': 'Пользователи (регистрация на курс)'},
        ),
        migrations.AlterField(
            model_name='teacher',
            name='img',
            field=models.ImageField(help_text='150x150px', null=True, upload_to='media/images/teachers', verbose_name='ссылка картинки'),
        ),
    ]
