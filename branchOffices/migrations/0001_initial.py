# Generated by Django 3.2.8 on 2021-11-14 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('doctors', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BranchOffices',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Nombre sucursal')),
                ('address', models.CharField(max_length=200, verbose_name='Direccion')),
                ('phone', models.IntegerField(verbose_name='Telefono')),
                ('image', models.ImageField(blank=True, null=True, upload_to='branchOffices/', verbose_name='Imagen')),
                ('description', models.TextField()),
                ('doctors', models.ManyToManyField(to='doctors.Doctor')),
                ('specialty', models.ManyToManyField(to='doctors.Specialty')),
            ],
            options={
                'verbose_name': 'branchOffice',
                'verbose_name_plural': 'branchOffices',
                'db_table': 'branchOffice',
            },
        ),
    ]
