from django.db import models
from doctors.models import Specialty
from usersApp.models import Usuario
from branchOffices.models import BranchOffices


class Appointment(models.Model):
    specialty = models.ForeignKey(Specialty, on_delete=models.CASCADE)
    date = models.DateField()
    branchOffices = models.ForeignKey(BranchOffices, on_delete=models.CASCADE,null=True,blank=True)

    def __str__(self):
        return str(self.name)


    class Meta:
        db_table = 'appointment'
        verbose_name = 'appointment'
        verbose_name_plural = 'appointments'