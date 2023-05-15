# Generated by Django 4.1.5 on 2023-05-11 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('v_kraskah', '0008_category_full_description_alter_category_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='full_description',
            field=models.TextField(blank=True, help_text='Полный текст курса', max_length=1000, verbose_name='полное описание'),
        ),
    ]
