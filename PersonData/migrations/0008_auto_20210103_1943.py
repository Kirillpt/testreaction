# Generated by Django 3.1.4 on 2021-01-03 19:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PersonData', '0007_auto_20201222_1903'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='test_variant',
            field=models.CharField(choices=[('E', 'Electro'), ('C', 'Computer'), ('V', 'Vibration'), ('SR', 'StereoSoundRight'), ('SL', 'StereoSoundLeft'), ('M', 'MonoSound'), ('PP', 'PicturePress'), ('PR', 'PictureRelease')], default='E', max_length=30, verbose_name='Вариант Теста'),
        ),
    ]
