from django.db import models
from django.contrib.auth.models import(BaseUserManager,AbstractBaseUser,PermissionsMixin)

class User(AbstractBaseUser,PermissionsMixin):
    email = models.EmailField(max_length=250,unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    #is_verified = models.BooleanField(default=False)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.email
    
