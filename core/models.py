import uuid

from django.db import models

from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import BaseUserManager

def get_file_path(_instance, filename):
    ext = filename.split('.')[-1]
    filename = f'{uuid.uuid4()}.{ext}'
    return filename

class UsuarioManager(BaseUserManager):

    use_in_migrations = True


    def _create_user(self, email, password, **extra_fields):

        if not email:
            raise ValueError('O campo email precisa ser preenchido')

        email = self.normalize_email(email)
        user = self.model(username=email, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self.db)
        return user

    def create_user(self, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser precisa ter is_staff=True')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser precisa ter is_superuser=True.')

        return self._create_user(email, password, **extra_fields)


# usuario customizado
class CustomUsuario(AbstractUser):

    email = models.EmailField('E-mail', unique=True)
    imagem = models.FileField('Imagem', upload_to=get_file_path, max_length=50, blank=True)
    first_name = models.CharField('Primeiro nome', max_length=150)
    last_name = models.CharField('Ultimo nome', max_length=150)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    def __str__(self):
        return self.email

    def get_imagem(self):
        if self.imagem:
            return self.imagem.url
        else:
            return "/static/img/blank-profile.png"

    objects = UsuarioManager()

