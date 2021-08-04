from core.email_sender import EmailMessage
from django.test import TestCase
from decouple import config

EMAIL_TEST = config('EMAIL_TEST')

class EmailSenderTestCase(TestCase):

    def setUp(self):
        self.data = {
            'first_name': 'Felicity',
            'last_name': 'Jones',
            'username': EMAIL_TEST,
            'password1': 'cc_kk_ll_nn2',
            'password2': 'cc_kk_ll_nn2'
        }




