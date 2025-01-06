from django.db import models
from django.contrib.auth.models import AbstractUser,BaseUserManager,Group,Permission

class UserManager(BaseUserManager):
  def create_user(self,email,password=None):
    if not email:
      raise ValueError('User must have an email address')
    user = self.model(email=self.normalize_email(email))
    user.set_password(password)
    user.save(using=self._db)
    return user
  def create_superuser(self,email,password):
    user = self.create_user(email,password=password)
    user.is_superuser = True
    user.is_staff = True
    user.save(using=self._db)
    return user
  
class User(AbstractUser):
  email = models.EmailField(unique=True,max_length=255)
  username = models.CharField(max_length=255,unique=False) 
  bio = models.TextField(blank=True, null=True)  
  profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True) 
  followers = models.ManyToManyField('self', symmetrical=False, related_name='following', blank=True)  
  groups = models.ManyToManyField(
        Group,
        related_name='custom_user_groups',  # Custom related_name to avoid clashes
        blank=True
    )
  user_permissions = models.ManyToManyField(
        Permission,
        related_name='custom_user_permissions',  # Custom related_name to avoid clashes
        blank=True
    )
  USERNAME_FIELD = 'email'
  REQUIRED_FIELDS = ['username']
  object = UserManager()
