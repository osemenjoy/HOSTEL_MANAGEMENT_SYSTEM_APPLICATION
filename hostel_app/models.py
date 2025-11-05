from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin


class UserManager(BaseUserManager):
    def create_user(self, matric_number, password=None, **extra_fields):
        if not matric_number:
            raise ValueError('Matric number is required')
        matric_number = str(matric_number)
        user = self.model(matric_number=matric_number, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, matric_number, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(matric_number, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    matric_number = models.CharField(max_length=30, unique=True)
    first_name = models.CharField(max_length=150, blank=True)
    last_name = models.CharField(max_length=150, blank=True)
    email = models.EmailField(blank=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'matric_number'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.matric_number
