# Generated by Django 2.1.5 on 2020-01-15 20:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20200115_2316'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='car',
            options={'ordering': ['-id'], 'verbose_name': 'Машина', 'verbose_name_plural': 'Машины'},
        ),
        migrations.AlterModelOptions(
            name='review',
            options={'ordering': ['-id'], 'verbose_name': 'Обзор', 'verbose_name_plural': 'Обзоры'},
        ),
    ]