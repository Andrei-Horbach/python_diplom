# Generated by Django 4.1.5 on 2023-05-11 18:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('v_kraskah', '0009_alter_category_full_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='groups',
            name='price',
            field=models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=10),
            preserve_default=False,
        ),
    ]
