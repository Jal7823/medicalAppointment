# Generated by Django 3.2.8 on 2021-12-08 22:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usersApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='image',
            field=models.ImageField(blank=True, default='perfil/', null=True, upload_to='perfil/', verbose_name='image de perfil'),
        ),
    ]
