# Generated by Django 2.1.7 on 2019-02-16 18:16

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('enderecos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='endereco',
            name='bairro',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='endereco',
            name='cep',
            field=models.CharField(blank=True, max_length=9, null=True),
        ),
        migrations.AddField(
            model_name='endereco',
            name='cidade',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='endereco',
            name='complemento',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='endereco',
            name='estado',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='endereco',
            name='latitude',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='endereco',
            name='logradouro',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='endereco',
            name='longitude',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='endereco',
            name='numero',
            field=models.SmallIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='endereco',
            name='pais',
            field=models.CharField(blank=True, max_length=70, null=True),
        ),
    ]
