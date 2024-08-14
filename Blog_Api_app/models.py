from django.db import models
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin
import os
from django.conf import settings
from django.template.defaultfilters import slugify

def get_image_filename(instance,filename):
    name = instance.user.email
    slug = slugify(name)
    return f"products/{slug}-{filename}"

class profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    avtar = models.ImageField(upload_to=get_image_filename,blank=True)
    bio = models.CharField(max_length=200,blank=True)

    def __str__(self):
        return self.user.email
    @property
    def filename(self):
        return os.path.basename(self.image.name)
from django.contrib.auth.base_user import BaseUserManager

class CustomUserManager(BaseUserManager):
    def create_user(self,email,username,password=None,**extra_fields):
        if not email:
            raise ValueError("User must have an email address")
        user = self.model(
            email = self.normalize_email(email),
            username = username
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self,email,username,password=None,**extra_fields):
        user = self.create_user(
            email,
            password=password,
            username=username
            
        )
        user.is_superuser = True
        user.save(using=self._db)
        return user


class CustomUser(AbstractBaseUser,PermissionsMixin):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=255)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    objects = CustomUserManager()
    def __str__(self):
        return self.email

# Create your models here.
