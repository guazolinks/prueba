# Generated by Django 4.2.2 on 2023-07-24 12:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('noticias', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='noticia',
            name='categoria',
        ),
        migrations.AddField(
            model_name='noticia',
            name='categoria',
            field=models.ManyToManyField(to='noticias.categoria'),
        ),
    ]
