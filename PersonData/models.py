from django.db import models

class Person(models.Model):
    GENDER_CHOICE = [
        ('M', 'Man'),
        ('F', 'Female'),
    ]
    name = models.CharField("ФИО", blank=True, max_length=40)
    gender = models.CharField("Пол", max_length=1, choices=GENDER_CHOICE)
    age = models.IntegerField()
    react_time = models.IntegerField()
    date = models.DateField()
    e_voltage = models.FloatField("Напряжение")

