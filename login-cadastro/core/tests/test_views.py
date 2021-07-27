from django.test import TestCase
from django.test import Client
from django.urls import reverse_lazy
from core.forms import CustomUsuarioCreateForm

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

    def test_post_function(self):
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
