from django.db import models


class Specialty(models.Model):
    name = models.CharField("Especialidad", max_length=100)
    image = models.ImageField('Imagen', upload_to='specialty/',null=True,blank=True)
    icon = models.CharField(max_length=100,blank=True, null=True)

    def __str__(self):
        return self.name





class Doctor(models.Model):
    name = models.CharField('Nombre', max_length=50)
    lastName = models.CharField('Apellido', max_length=50)
    medicalNumber = models.IntegerField('Nro. Medico')
    specialty = models.ManyToManyField(Specialty)
    image = models.ImageField('Imagen', upload_to='doctors/', null=True,blank=True)

    def __str__(self):
        return self.name


class Patology(models.Model):
    name = models.CharField('Patologia', max_length=100)

    def __str__(self):
        return self.name


class Exam(models.Model):
    name = models.CharField('Examen', max_length=100)
    result = models.BooleanField('Resultado')

    def __str__(self):
        return self.name


