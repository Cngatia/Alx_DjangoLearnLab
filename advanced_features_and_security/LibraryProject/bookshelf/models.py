# relationship_app/models.py
from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager

class CustomUserManager(BaseUserManager):
    def create_user(self, username, email, date_of_birth, profile_photo, password=None):
        if not email:
            raise ValueError("The Email field must be set")
        email = self.normalize_email(email)
        user = self.model(username=username, email=email, date_of_birth=date_of_birth, profile_photo=profile_photo)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, date_of_birth, profile_photo, password=None):
        user = self.create_user(username, email, date_of_birth, profile_photo, password)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user

class CustomUser(AbstractUser):
    date_of_birth = models.DateField()
    profile_photo = models.URLField()

    objects = UserManager()

    def __str__(self):
        return self.username

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'date_of_birth', 'profile_photo']
# bookshelf/models.py
from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=200)

    class Meta:
        permissions = [
            ("can_create", 'Can create book'),
            ("can_delete", 'Can delete book'),
            ("can_edit", 'Can edit book'),
            ("can_view", 'Can view book'),
        ]

    def __str__(self):
        return self.title