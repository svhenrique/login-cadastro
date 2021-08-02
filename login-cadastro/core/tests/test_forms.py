from django.test import TestCase
from model_mommy import mommy
from core.forms import CustomPasswordResetForm, CustomUsuarioCreateForm
from core.email_sender import EmailMessage
from django.template import loader
from decouple import config

EMAIL_TEST = config('EMAIL_TEST')

class CustomPasswordResetFormTestCase(TestCase):

    def setUp(self):
        self.first_name = 'Felicity',
        self.last_name = 'Jones',
        self.username = EMAIL_TEST
        self.password = "cc_kk_ll_nn2"
        self.data = {
            "first_name": self.first_name,
            "last_name": self.last_name,
            "username": self.username,
            "password1": self.password,
            "password2": self.password
        }
        self.form = CustomPasswordResetForm(data={"email": self.username})

    def test_send_mail_status_code(self):
        response = self.form.send_mail(data=self.data)
        self.assertEquals(response, 202)

    def test_form_valid(self):
        form = self.form
        self.assertEquals(form.is_valid(), True)

class CustomUsuarioCreateFormTestCase(TestCase):

    def setUp(self):
        self.first_name = 'Felicity',
        self.last_name = 'Jones',
        self.username = 'felicity@gmail.com'
        self.password = "cc_kk_ll_nn2"
        self.data = {
            "first_name": self.first_name,
            "last_name": self.last_name,
            "username": self.username,
            "password1": self.password,
            "password2": self.password
        }
        self.create_form = CustomUsuarioCreateForm(data=self.data)

    def test_form_valid(self):
        form = self.create_form
        valid = form.is_valid()
        self.assertTrue(valid)

    def test_form_creation(self):
        form = self.create_form
        form.is_valid()
        user = form.save()
        self.assertIsNotNone(user.id)


