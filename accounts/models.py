from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    ROLE_CHOICES = [
        ('admin',    'Admin'),
        ('citizen',  'Citizen'),
        ('observer', 'Election Observer'),
    ]
    role   = models.CharField(max_length=20, choices=ROLE_CHOICES, default='citizen')
    phone  = models.CharField(max_length=15, blank=True)
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True)

    class Meta:
        verbose_name = 'User'

    def __str__(self):
        return f'{self.username} ({self.get_role_display()})'

    @property
    def is_admin(self):    return self.role == 'admin'

    @property
    def is_citizen(self):  return self.role == 'citizen'

    @property
    def is_observer(self): return self.role == 'observer'