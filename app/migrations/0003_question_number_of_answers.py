# Generated by Django 3.2 on 2021-04-16 21:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_rename_likeanswers_likeanswer'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='number_of_answers',
            field=models.IntegerField(default=0, verbose_name='Количество ответов'),
        ),
    ]