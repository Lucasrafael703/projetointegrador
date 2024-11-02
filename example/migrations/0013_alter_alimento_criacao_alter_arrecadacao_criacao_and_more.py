# Generated by Django 4.1.3 on 2024-11-02 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('example', '0012_alter_alimento_criacao'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alimento',
            name='criacao',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='arrecadacao',
            name='criacao',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='arrecadacao_alimento',
            name='criacao',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='arrecadacao_eletrodomestico',
            name='criacao',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='arrecadador',
            name='criacao',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='eletrodomestico',
            name='criacao',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='genero',
            name='criacao',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='tamanho',
            name='criacao',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='vestuario',
            name='criacao',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
