from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)
from django.core.exceptions import ValidationError


class UserManager(BaseUserManager):
    use_in_migrations=True
    def create_user(self, username, name, designation, password):
        user = self.model(
            username = username,
            name = name,
            designation = designation,
        )
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, username, name, designation, password):
        
        if not designation=='Hall Manager':
            raise ValidationError('Only Hall Manager can be a admin')
        else:
            user = self.model(
                name = name,
                designation = designation,
                username = username,
            )
            user.set_password(password)
            user.save()
            user.is_admin = True
            user.set_password(password)
            user.save()
            return user


class User_class(AbstractBaseUser):
    is_admin = models.BooleanField(default=False)
    objects = UserManager()
    name = models.CharField(max_length=50)
    Designation_Choices = (('Student','Student'),('Hall Manager','Hall Manager'),('Mess Manager','Mess Manager'),('Canteen Manager','Canteen Manager'), ('Sports Secy', 'Sports Secy'))
    designation = models.CharField(
        max_length=15,
        choices=Designation_Choices,
    )
    username = models.CharField(max_length=20, unique=True, blank=True)
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['name', 'designation']

    def __str__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        if self.designation == "Hall Manager":
            return True
        if perm==self.designation:
            return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin