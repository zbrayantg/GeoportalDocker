# Generated by Django 3.2.9 on 2022-03-29 21:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('BIF', '0005_auto_20220224_1027'),
    ]

    operations = [
        migrations.CreateModel(
            name='Licence',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('curation', models.CharField(blank=True, max_length=100, null=True)),
                ('modality', models.CharField(blank=True, max_length=100, null=True)),
                ('type_construction', models.CharField(blank=True, max_length=100, null=True)),
                ('licence_number', models.CharField(blank=True, max_length=100, null=True)),
                ('licence_date', models.DateField(blank=True, null=True)),
                ('construction_date', models.DateField(blank=True, null=True)),
                ('area', models.FloatField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Licencia',
                'verbose_name_plural': 'Licencias',
            },
        ),
        migrations.CreateModel(
            name='Occupancy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('owner', models.CharField(blank=True, max_length=100, null=True)),
                ('contract', models.CharField(blank=True, max_length=100, null=True)),
                ('type_occupancy', models.CharField(blank=True, max_length=100, null=True)),
                ('id_document', models.CharField(blank=True, max_length=100, null=True)),
                ('ocuppancy_document', models.CharField(blank=True, max_length=100, null=True)),
                ('ocuppancy_name', models.CharField(blank=True, max_length=100, null=True)),
                ('seppi', models.CharField(blank=True, max_length=100, null=True)),
                ('observation', models.TextField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Ocupación',
                'verbose_name_plural': 'Ocupaciones',
            },
        ),
        migrations.CreateModel(
            name='Property',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('predial', models.CharField(blank=True, max_length=60, null=True)),
                ('alternative_predial', models.CharField(blank=True, max_length=60, null=True)),
                ('appraisal', models.CharField(blank=True, max_length=60, null=True)),
                ('document_type', models.CharField(blank=True, max_length=100, null=True)),
                ('act', models.CharField(blank=True, max_length=100, null=True)),
                ('document_number', models.CharField(blank=True, max_length=50, null=True)),
                ('real_state_register', models.CharField(blank=True, max_length=100, null=True)),
                ('document_date', models.DateField(blank=True, null=True)),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Fecha de actualización')),
                ('coordenadas', models.TextField(blank=True, null=True)),
                ('archivo', models.FileField(blank=True, null=True, upload_to='staticfiles/files')),
            ],
            options={
                'verbose_name': 'Propiedad',
                'verbose_name_plural': 'Propiedades',
            },
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(blank=True, max_length=50, null=True)),
                ('category', models.CharField(blank=True, max_length=100, null=True)),
                ('type_property', models.CharField(blank=True, max_length=100, null=True)),
                ('name', models.CharField(blank=True, max_length=200, null=True)),
                ('video', models.TextField(blank=True, null=True)),
                ('addres', models.TextField(blank=True, null=True)),
                ('class_property', models.CharField(blank=True, max_length=50, null=True)),
                ('use', models.CharField(blank=True, max_length=100, null=True)),
                ('id_property', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='BIF.property')),
            ],
            options={
                'verbose_name': 'Situación del inmueble',
                'verbose_name_plural': 'Situación de los inmuebles',
            },
        ),
        migrations.DeleteModel(
            name='Inmueble',
        ),
        migrations.AddField(
            model_name='occupancy',
            name='id_property',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='BIF.property'),
        ),
        migrations.AddField(
            model_name='licence',
            name='id_property',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='BIF.property'),
        ),
    ]
