# Generated by Django 2.1.5 on 2020-01-10 05:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='scopes',
            field=models.ManyToManyField(related_name='tags', through='articles.ArticleScope', to='articles.Scope'),
        ),
    ]
