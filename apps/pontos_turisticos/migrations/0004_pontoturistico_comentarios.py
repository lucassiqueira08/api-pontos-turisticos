# Generated by Django 2.1.7 on 2019-02-16 17:14

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('comentarios', '0001_initial'),
        ('pontos_turisticos', '0003_pontoturistico_atracoes'),
    ]

    operations = [
        migrations.AddField(
            model_name='pontoturistico',
            name='comentarios',
            field=models.ManyToManyField(to='comentarios.Comentario'),
        ),
    ]
