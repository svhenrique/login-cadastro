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

