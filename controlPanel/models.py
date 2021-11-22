from django.db import models

# Create your models here.



class Simbolic(models.Model):
    name = models.CharField('Nombre', max_length=50)

    def __str__(self):
        return self.name