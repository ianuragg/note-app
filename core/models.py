from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.utils import timezone

#User Management
class MyUserManager(BaseUserManager):
    use_in_migrations: True

    #Create User
    def create_user(self, email, password, **extra_fields):
        if not email:
            return ValueError("User must have an email addresss")
        
        now = timezone.now()

        user = self.model(
            email = self.normalize_email(email),
            date_joined = now,
            last_login = now,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    #Create Superuser
    def create_superuser(self, email, password):
        user = self.create_user(
            email=self.normalize_email(email),
            password=password
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

        return user

#User Model
class User(AbstractBaseUser):
    email = models.EmailField(max_length=254, unique=True, verbose_name="Email")
    name = models.CharField(max_length=30, verbose_name="Name")
    date_joined = models.DateTimeField(verbose_name="date joined", auto_now_add=True)
    last_login = models.DateTimeField(verbose_name="last login", auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'

    objects = MyUserManager()

    def __str__(self):
        return self.name + " - " + self.email

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True

#Note Model
class Note(models.Model):
    user_note = models.ForeignKey(User, on_delete = models.CASCADE, related_name='user_note')
    title = models.CharField(max_length=200, verbose_name="Note Title")
    description = models.TextField(max_length=500, verbose_name="Note Description")
    date_added = models.DateTimeField(verbose_name="Date Added", auto_now_add=True)
    is_active = models.BooleanField(default=True)