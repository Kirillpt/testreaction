# Generated by Django 3.1.4 on 2020-12-14 19:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PersonData', '0002_auto_20201214_1914'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='date',
            field=models.DateTimeField(auto_now=True, verbose_name='Дата и Время Регистрации'),
        ),
    ]