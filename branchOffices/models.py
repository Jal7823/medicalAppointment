from django.db import models
from doctors.models import Doctor, Specialty
from ckeditor.fields import RichTextField


class BranchOffices(models.Model):
    name = models.CharField('Nombre sucursal', max_length=50)
    address = models.CharField('Direccion', max_length=200)
    phone = models.IntegerField('Telefono')
    doctors = models.ManyToManyField(Doctor)
    specialty = models.ManyToManyField(Specialty)
    image = models.ImageField('Imagen', upload_to='branchOffices/', null=True, blank=True)
    description = models.TextField()

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'branchOffice'
        verbose_name = 'branchOffice'
        verbose_name_plural = 'branchOffices'
