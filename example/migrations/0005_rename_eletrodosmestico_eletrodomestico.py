# Generated by Django 4.1.3 on 2024-10-16 19:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('example', '0004_rename_eletrodosmesticos_eletrodosmestico_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Eletrodosmestico',
            new_name='Eletrodomestico',
        ),
    ]
