import uuid

from django.db import models

from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import BaseUserManager

from django.dispatch import receiver
import os

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
    image = models.ImageField('Imagem', upload_to=get_file_path, max_length=50, blank=True)
    first_name = models.CharField('Primeiro nome', max_length=150)
    last_name = models.CharField('Ultimo nome', max_length=150)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    def __str__(self):
        return self.email

    def get_image(self):
        if self.image:
            return self.image.url
        else:
            return "/static/img/blank-profile.png"

    objects = UsuarioManager()

@receiver(models.signals.pre_delete, sender=CustomUsuario)
def delete_image_pre_user_delete(instance, **kwargs):
    if instance.image:
        if os.path.isfile(instance.image.path):
            os.remove(instance.image.path)

@receiver(models.signals.pre_save, sender=CustomUsuario)
def delete_image_pre_user_change(instance, **kwargs):
    """
        This functions analizes if an image of a user in database is equals
        to the instance's image.

        This is important because when login opereration is made, the pre_save
        signal is called, therefore, this verification is required to not erase image
        of user which is used in database.
    """

    if CustomUsuario.objects.filter(pk=instance.pk).exists():

        user_in_db = CustomUsuario.objects.get(pk=instance.pk)

        if user_in_db.image:
            if user_in_db.image != instance.image:
                if os.path.isfile(user_in_db.image.path):
                    print('image deletada |'*50)
                    os.remove(user_in_db.image.path)


