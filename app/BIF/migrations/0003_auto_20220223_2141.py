# Generated by Django 3.2.9 on 2022-02-24 02:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BIF', '0002_rename_num_escritura_inmueble_numero_escritura'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='inmueble',
            name='latitud',
        ),
        migrations.RemoveField(
            model_name='inmueble',
            name='longitud',
        ),
        migrations.AddField(
            model_name='inmueble',
            name='coordenadas',
            field=models.TextField(blank=True, null=True),
        ),
    ]
