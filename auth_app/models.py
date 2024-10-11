from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth.models import BaseUserManager

class CustomUserManager(BaseUserManager):
    def create_user(self, username, email, password=None, **extra_fields):
        """
        Crea y guarda un usuario regular.
        """
        if not username:
            raise ValueError('El nombre de usuario debe ser proporcionado')
        if not email:
            raise ValueError('El correo electrónico debe ser proporcionado')

        email = self.normalize_email(email)
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password=None, **extra_fields):
        """
        Crea y guarda un superusuario con rol de admin.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('role', 'admin')  # Asigna el rol 'admin'

        if extra_fields.get('is_staff') is not True:
            raise ValueError('El superusuario debe tener is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('El superusuario debe tener is_superuser=True.')

        return self.create_user(username, email, password, **extra_fields)

class CustomUser(AbstractUser):
    ROLE_CHOICES = (
        ('admin', 'Admin'),
        ('supervisor', 'Supervisor'),
        ('vendedor', 'Vendedor'),
    )
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='vendedor')
    estado = models.IntegerField(default=1)

    objects = CustomUserManager()  # Asigna el manager personalizado

    def is_admin(self):
        return self.role == 'admin'

    def is_supervisor(self):
        return self.role == 'supervisor'

    def is_vendedor(self):
        return self.role == 'vendedor'