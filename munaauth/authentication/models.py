# authentication/models.py

from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    SUPER_ADMIN = 'super_admin'
    DEVELOPER = 'developer'
    MANAGER = 'manager'
    OPERATOR = 'operator'
    MEMBER = 'member'

    ROLE_CHOICES = [
        (SUPER_ADMIN, 'Super Admin'),
        (DEVELOPER, 'Developer'),
        (MANAGER, 'Manager'),
        (OPERATOR, 'Operator'),
        (MEMBER, 'Member'),
    ]

    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default=MEMBER)
