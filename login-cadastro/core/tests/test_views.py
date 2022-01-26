from django.test import TestCase
from django.test import Client
from django.urls import reverse_lazy
from core.forms import CustomUsuarioCreateForm
from core.models import CustomUsuario
from decouple import config
from model_mommy import mommy

EMAIL_TEST = config('EMAIL_TEST')

class IndexViewTestCase(TestCase):

    def setUp(self):
        self.data = {
            'first_name': 'Felicity',
            'last_name': 'Jones',
            'username': 'felicity@gmail.com',
            'password1': 'cc_kk_ll_nn2',
            'password2': 'cc_kk_ll_nn2'
        }
        self.user_creation_form = CustomUsuarioCreateForm(data=self.data)
        self.client = Client()

    def test_get_function(self):
        request = self.client.get(reverse_lazy('index'), follow=True)
        redirects = len(request.redirect_chain)
        self.assertEquals(redirects, 1)

    def test_get_function_when_login(self):
        self.user_creation_form.is_valid()
        self.user_creation_form.save()
        data = {
            'username': self.data['username'],
            'password': self.data['password1']
        }
        client = self.client.login(username=data['username'], password=data['password'])
        request = self.client.get(reverse_lazy('index'), follow=True)
        redirects = len(request.redirect_chain)
        self.assertEquals(redirects, 0)

class RegisterViewTestCase(TestCase):

    def setUp(self):
        self.data = {
            'first_name': 'Felicity',
            'last_name': 'Jones',
            'username': 'felicity@gmail.com',
            'password1': 'cc_kk_ll_nn2',
            'password2': 'cc_kk_ll_nn2'
        }
        self.user_creation_form = CustomUsuarioCreateForm(data=self.data)
        self.client = Client()

    def test_get_anonymous(self):
        request = self.client.get(reverse_lazy('register'), follow=True)
        redirects = len(request.redirect_chain)
        self.assertEquals(redirects, 0)

    def test_get_logged(self):
        self.user_creation_form.is_valid()
        self.user_creation_form.save()
        client = self.client.login(username=self.data['username'], password=self.data['password1'])
        client = self.client.get(reverse_lazy('register'), follow=True)
        redirects = len(client.redirect_chain)
        self.assertEquals(redirects, 1)

    def test_user_creation(self):
        response = self.client.post(reverse_lazy('register'), self.data)
        users = CustomUsuario.objects.all()
        self.assertEquals(len(users), 1)

    def test_equal_user_creation(self):
        self.user_creation_form.is_valid()
        self.user_creation_form.save()
        response = self.client.post(reverse_lazy('register'), self.data)
        users = CustomUsuario.objects.all()
        self.assertEquals(len(users), 1)

class PasswordResetViewTestCase(TestCase):

    def setUp(self):
        self.user = mommy.make('CustomUsuario', username=EMAIL_TEST, email=EMAIL_TEST)
        self.client = Client()

    def test_email_password_reset(self):
        self.user.save()
        client = self.client.post(reverse_lazy('password_reset'), data={'email': EMAIL_TEST})
        response = client.status_code
        self.assertEquals(response, 302)