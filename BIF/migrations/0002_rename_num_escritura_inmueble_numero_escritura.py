# Generated by Django 3.2.9 on 2022-02-23 04:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('BIF', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='inmueble',
            old_name='num_escritura',
            new_name='numero_escritura',
        ),
    ]
