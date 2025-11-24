from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    ROLE_CHOICES = (
        ('user','Пользователь'),
        ('admin','Администратор'),
    )
    role = models.CharField(choices=ROLE_CHOICES, default='user', max_length=20)