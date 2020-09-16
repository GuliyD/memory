from django.db import models
from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin


class PersonManager(BaseUserManager):
    def create_user(self, email, username, password=None):
        if not email:
            raise ValueError('User must have email')
        if not username:
            raise ValueError('User must have username')

        user = self.model(
            email=self.normalize_email(email),
            username=username
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password=None):
        user = self.create_user(
            email=email,
            username=username,
            password=password
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class Person(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=60, unique=True)
    username = models.CharField(max_length=60)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    objects = PersonManager()

    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = ['username']


class Task(models.Model):
    theme = models.CharField(max_length=120, default='none theme')
    text = models.TextField()
    last_update = models.DateTimeField(auto_now=True)
    person = models.ForeignKey(Person, on_delete=models.CASCADE, related_name='tasks')


class Contact(models.Model):
    name = models.CharField(max_length=60)
    surname = models.CharField(max_length=60, blank=True, null=True)
    birthday = models.DateField(blank=True, null=True)
    notes = models.TextField(blank=True, null=True)
    person = models.ForeignKey(Person, on_delete=models.CASCADE, related_name='contacts')


class ContactPhoto(models.Model):
    photo = models.ImageField()
    contact = models.ForeignKey(Contact, on_delete=models.CASCADE)


class ContactPhoneNumber(models.Model):
    phone_number = models.CharField(max_length=30)
    contact = models.ForeignKey(Contact, on_delete=models.CASCADE)
