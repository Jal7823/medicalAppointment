from django.conf import settings
from django.db import models
from django_userforeignkey.models.fields import UserForeignKey


from branchOffices.models import BranchOffices
from doctors.models import Specialty
from django.contrib.auth.models import User




class Appointment(models.Model):
    user = UserForeignKey(auto_user_add=True) 
    name = models.CharField('Nombre', max_length=100,null=True,blank=True)
    lastName = models.CharField('Apellido', max_length=100,null=True,blank=True)
    dni = models.IntegerField('DNI',null=True,blank=True)
    specialty = models.ForeignKey(Specialty, on_delete=models.CASCADE)
    date = models.DateField()
    branchOffices = models.ForeignKey(BranchOffices, on_delete=models.CASCADE,null=True,blank=True)

    def __str__(self):
        return str(self.name)


    class Meta:
        db_table = 'appointment'
        verbose_name = 'appointment'
        verbose_name_plural = 'appointments'