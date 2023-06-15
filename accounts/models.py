from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings


class User(AbstractUser):
    profile_picture = models.ImageField(upload_to='profile_pictures/')
    address = models.CharField(max_length=255)

    class Meta:
        db_table = 'custom_user'
        swappable = 'AUTH_USER_MODEL'
        default_permissions = ()
        permissions = (('view_user', 'Can view user'),)

User._meta.get_field('user_permissions').related_name = 'custom_user_permissions'


class Patient(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)


class Doctor(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

