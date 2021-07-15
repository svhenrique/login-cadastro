import uuid
from django.test import TestCase

from model_mommy import mommy
from core.models import get_file_path

class GetFilePathTestCase(TestCase):

    def setUp(self):
        self.filename = f'{uuid.uuid4()}.png'

    def test_get_file_path(self):
        file = get_file_path(None, 'teste.png')
        self.assertTrue(len(file), len(self.filename))

class CustomUsuarioTestCase(TestCase):

    def setUp(self):
        self.usuario = mommy.make('CustomUsuario')

    def test_str(self):
        self.assertEquals(str(self.usuario), self.usuario.email)

    def test_image_url(self):
        self.assertEquals("/static/img/blank-profile.png", self.usuario.get_imagem())


