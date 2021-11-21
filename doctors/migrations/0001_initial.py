# Generated by Django 3.2.8 on 2021-11-21 13:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Exam',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Examen')),
                ('result', models.BooleanField(verbose_name='Resultado')),
            ],
        ),
        migrations.CreateModel(
            name='Patology',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Patologia')),
            ],
        ),
        migrations.CreateModel(
            name='Specialty',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Especialidad')),
                ('image', models.ImageField(blank=True, null=True, upload_to='specialty/', verbose_name='Imagen')),
                ('icon', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Nombre')),
                ('lastName', models.CharField(max_length=50, verbose_name='Apellido')),
                ('medicalNumber', models.IntegerField(verbose_name='Nro. Medico')),
                ('image', models.ImageField(blank=True, null=True, upload_to='doctors/', verbose_name='Imagen')),
                ('specialty', models.ManyToManyField(to='doctors.Specialty')),
            ],
        ),
    ]
