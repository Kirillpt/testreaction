from django.db import models

class Person(models.Model):
    GENDER_CHOICE = [
        ('M', 'Man'),
        ('F', 'Female'),
    ]
    TEST_VARIANT = [
        ("E", "Electro"),
        ("C", "Computer"),
        ("V", "Vibration"),
        ("SR", "StereoSoundRight"),
        ("SL", "StereoSoundLeft"),
        ("M", "MonoSound"),
        ("PP", "PicturePress"),
        ("PR", "PictureRelease"),
    ]
    name = models.CharField("ФИО", default="anonimous", max_length=40)
    gender = models.CharField("Пол", max_length=1, choices=GENDER_CHOICE)
    age = models.IntegerField("Возраст")
    react_time = models.IntegerField("Время Реакции")
    test_variant = models.CharField("Вариант Теста",default="E", max_length=30, choices=TEST_VARIANT) 
    e_voltage = models.FloatField("Напряжение", blank=True, default=0)

