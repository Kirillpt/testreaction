from django.db import models

class Person(models.Model):
    GENDER_CHOICE = [
        ('M', 'Man'),
        ('F', 'Female'),
    ]
    name = models.CharField("ФИО", default="anonimous", max_length=40)
    gender = models.CharField("Пол", max_length=1, choices=GENDER_CHOICE)
    age = models.IntegerField("Возраст")
    react_time = models.IntegerField("Время Реакции")
    date = models.DateTimeField("Дата и Время Регистрации");
    e_voltage = models.FloatField("Напряжение", blank=True, default=0)

