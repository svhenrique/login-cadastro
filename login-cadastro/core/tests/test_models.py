import uuid
from django.test import TestCase

from model_mommy import mommy
from core.models import get_file_path

from core.models import UsuarioManager, CustomUsuario

class GetFilePathTestCase(TestCase):

    def setUp(self):
        self.filename = f'{uuid.uuid4()}.png'

    def test_get_file_path(self):
        file = get_file_path(None, 'teste.png')
        self.assertTrue(len(file), len(self.filename))

class CustomUsuarioTestCase(TestCase):

    def setUp(self):
        self.user = mommy.make('CustomUsuario')
        self.user_with_image = mommy.make('CustomUsuario', image='teste.png')

    def test_str(self):
        self.assertEquals(str(self.user), self.user.email)

    def test_default_image_url(self):
        self.assertEquals("/static/img/blank-profile.png", self.user.get_image())

    def test_image_profile(self):
        self.assertEquals(self.user_with_image.image.url, self.user_with_image.get_image())

class UsuarioManagerTestCase(TestCase):

    def setUp(self):
        self.user = mommy.make('CustomUsuario')
        self.data = {
            'first_name': 'Teste',
            'last_name': 'dos Santos',
            'username': 'teste@gmail.com',
            'password': 'tt_@_3_@_2_4',
            'image': 'teste.png'
        }

    def test_user_is_staff(self):
        self.assertEquals(False, self.user.is_staff)

    def test_user_is_superuser(self):
        self.assertEquals(False, self.user.is_superuser)

    def test_user_creation(self):

        username = self.data['username']
        password = self.data['password']
        first_name = self.data['first_name']
        last_name = self.data['last_name']
        password = self.data['password']
        image = self.data['image']

        user = CustomUsuario.objects.create_user(username, password, first_name=first_name, image=image, last_name=last_name)
        user_in_db = CustomUsuario.objects.get(id=user.id)

        self.assertEquals(user, user_in_db)



