from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager

# Create your models here.

class UserProfileManager(BaseUserManager):
    """Helpps django work with our custom user model."""

    def create_user(self,email,name,password=None):
        if not email:
            raise ValueError('Users most have email adress.')


        email = self.normalize_email(email)
        user = self.model(email=email, name=name)

        user.set_password(password)
        user.save(using=self._db)

        return user
    
    def create_superuser(self,email,name,password):
        """Create and save a new superuser with given details."""

        user = self.create_user(email,name,password)
        
        user.is_superuser = True
        user.is_stuff = True

        user.save(using=self._db)

        return user

class UserProfile(AbstractBaseUser,PermissionsMixin):
    """Respents a 'user profile' inside our system."""

    email = models.EmailField(max_length=255,unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def get_full_name(self):
        """Use to get a user full name."""

        return self.name
    
    def get_short_name(self):
        """Used to get user short name."""

        return self.name
    
    def __str__(self):
        """Django uses this when it needs to convert the object to a string"""
        
        return self.email