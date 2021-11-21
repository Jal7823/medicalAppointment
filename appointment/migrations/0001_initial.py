# Generated by Django 3.2.8 on 2021-11-21 11:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('doctors', '0001_initial'),
        ('branchOffices', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True, verbose_name='Nombre')),
                ('lastName', models.CharField(blank=True, max_length=100, null=True, verbose_name='Apellido')),
                ('dni', models.IntegerField(blank=True, null=True, verbose_name='DNI')),
                ('date', models.DateField()),
                ('branchOffices', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='branchOffices.branchoffices')),
                ('specialty', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='doctors.specialty')),
            ],
            options={
                'verbose_name': 'appointment',
                'verbose_name_plural': 'appointments',
                'db_table': 'appointment',
            },
        ),
    ]
