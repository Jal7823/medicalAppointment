# Generated by Django 3.2.8 on 2021-11-13 22:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctors', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='specialty',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='specialty/', verbose_name='Imagen'),
        ),
    ]
