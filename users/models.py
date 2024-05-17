from django.db import models
from django.core.validators import EmailValidator, RegexValidator
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    username = models.CharField(max_length=150, unique=True, validators=[RegexValidator(
        regex='^[a-zA-Z0-9._]+$',
        message='Enter a valid username. This value may contain only letters, numbers, dots, and underscores.',
        code='invalid_username'
    )], db_index=True, verbose_name='Username')
    email = models.EmailField(unique=True, validators=[EmailValidator(message='Enter a valid email address.')], db_index=True, verbose_name='Email')
    password = models.CharField(max_length=128)
    first_name = models.CharField(max_length=55, verbose_name='First Name')
    last_name = models.CharField(max_length=55, verbose_name='Last Name')
    is_provider = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)

    def __str__(self):
        return self.username
