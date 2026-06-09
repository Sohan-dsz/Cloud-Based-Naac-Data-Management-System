from django.db import models
from django.contrib.auth.models import AbstractUser


class Role(models.Model):
    """Role model for role-based access control."""
    ROLE_CHOICES = [
        ('iqac_admin', 'IQAC Admin'),
        ('dept_admin', 'Department Admin'),
        ('faculty', 'Faculty'),
        ('student', 'Student'),
    ]

    name = models.CharField(max_length=20, choices=ROLE_CHOICES, unique=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.get_name_display()

    class Meta:
        verbose_name = 'Role'
        verbose_name_plural = 'Roles'


class User(AbstractUser):
    """Custom user model extending Django's AbstractUser."""
    groups = models.ManyToManyField('auth.Group', related_name='custom_users', blank=True)
    user_permissions = models.ManyToManyField('auth.Permission', related_name='custom_users', blank=True)
    roles = models.ManyToManyField(Role, related_name='users')
    keycloak_id = models.CharField(max_length=255, unique=True, blank=True, null=True)
    department = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'
