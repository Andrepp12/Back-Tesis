from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    ROLE_CHOICES = (
        ('admin', 'Admin'),
        ('supervisor', 'Supervisor'),
        ('vendedor', 'Vendedor'),
    )
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='vendedor')

    def is_admin(self):
        return self.role == 'admin'

    def is_supervisor(self):
        return self.role == 'supervisor'

    def is_vendedor(self):
        return self.role == 'vendedor'

    def create_superuser(self, *args, **kwargs):
        kwargs['role'] = 'admin'
        return super().create_superuser(*args, **kwargs)

