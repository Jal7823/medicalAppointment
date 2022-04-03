from django.conf.global_settings import MEDIA_URL, STATIC_URL
from django.contrib.auth.models import AbstractUser, BaseUserManager,PermissionsMixin
from doctors.models import Doctor,Patology
from django.db import models

class UsuarioManager(BaseUserManager):
    def create_user(self, email, username, name, password=None):
        if not email:
            raise ValueError('El usuario debe tener un correo electronico')

        user = self.model(
            username=username,
            email=self.normalize_email(email),
            name=name,
        )

        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, username, email, name, password):
        user = self.create_user(
            email,
            username=username,
            name=name,
            password=password,
        )

        user.user_administrator = True
        user.staff = True
        user.save()
        return user


class Usuario(AbstractUser):
    username = models.CharField('Nombre de usuario', unique=True, max_length=100)
    email = models.EmailField('Correo electronico',unique=True, max_length=254)
    name = models.CharField('Nombre', max_length=200, blank=True, null=True)
    lastName = models.CharField('lastName', max_length=200, blank=True, null=True)
    image = models.ImageField('image de perfil/', upload_to='perfil/', null=True, blank=True,default='perfil/undefined.jpg')
    usuar_active = models.BooleanField(default=True)
    user_administrator = models.BooleanField(default=False)
    staff = models.BooleanField(default=False)
    dni = models.IntegerField(verbose_name='DNI', blank=True, null=True)
    direc = models.CharField(max_length=300, verbose_name='Direccion', blank=True, null=True)
    loc = models.CharField(max_length=300, verbose_name='Localidad', blank=True, null=True)
    provincias = (
        ('C.A.B.A.', 'C.A.B.A.'),
        ('Buenos Aires', 'Buenos Aires',),
        ('Catamarca', 'Catamarca'),
        ('Chaco', 'Chaco'),
        ('Chubut', 'Chubut'),
        ('Córdoba', 'Córdoba'),
        ('Corrientes', 'Corrientes'),
        ('Entre Ríos', 'Entre Ríos'),
        ('Formosa', 'Formosa'),
        ('Jujuy', 'Jujuy'),
        ('La Pampa', 'La Pampa'),
        ('La Rioja', 'La Rioja'),
        ('Mendoza', 'Mendoza'),
        ('Misiones', 'Misiones'),
        ('Neuquén', 'Neuquén'),
        ('Río Negro', 'Río Negro'),
        ('Salta', 'Salta'),
        ('San Juan', 'San Juan'),
        ('Santa Cruz', 'Santa Cruz'),
        ('Santa Fe', 'Santa Fe'),
        ('Santiago del Estero', 'Santiago del Estero'),
        ('Tierra del Fuego', 'Tierra del Fuego'),
        ('Tucumán', 'Tucumán'),
    )
    pcia = models.CharField(max_length=300, choices=provincias,verbose_name='Provincia', blank=True, null=True)
    tlf = models.IntegerField(verbose_name='Telefono', blank=True, null=True)
    sick = models.BooleanField(default=False)
    doctors = models.ManyToManyField(Doctor,'Doctor',null=True,blank=True)
    patology = models.ManyToManyField(Patology,'Patologia',null=True,blank=True)
    history = models.TextField('Historia',null=True,blank=True)
    isDoctor = models.BooleanField(default=False)
    nrMembership = models.IntegerField(null=True,blank=True)

    objects = UsuarioManager()

    USER_NAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'name']

    def __str__(self):
        return f'{self.name}  {self.last_name}'.upper()

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, usuarios_label):
        return True

    @property
    def is_staff(self):
        return self.user_administrator

    @property
    def is_superuser(self):
        return self.user_administrator

    def full_name(self):
        return f'{self.name} {self.lastName}'




