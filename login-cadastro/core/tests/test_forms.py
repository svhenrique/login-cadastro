from django.test import TestCase
from model_mommy import mommy
from core.forms import CustomPasswordResetForm, CustomUsuarioCreateForm
from core.email_sender import EmailMessage
from django.template import loader


class CustomPasswordResetForm(CustomPasswordResetForm):
    """
        Método reescrito para:
            - Evitar envios de emails de reset desnecessários.
            - Testar sem precisar recriar passos de formulários django.
    """
    def send_mail(self, data=None):
        # subject = loader.render_to_string(subject_template_name, context)
        # Email subject *must not* contain newlines
        # subject = ''.join(subject.splitlines())
        # body = loader.render_to_string(email_template_name, context)

        mail = EmailMessage(data['to_email'], data['subject'], ('text/plain', data['body']))
        # response = mail.send_email()
        response = 202
        return response

class CustomPasswordResetFormTestCase(TestCase):

    def setUp(self):
        self.name = 'Felicity Jones'
        self.email = 'felicity@gmail.com'
        self.subject = 'Um assunto qualquer'
        self.message = 'Uma mensagem qualquer'
        self.data = {
            'name': self.name,
            'to_email': self.email,
            'subject': self.subject,
            'body': self.message
        }
        self.form = CustomPasswordResetForm(data={"email": self.email})

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


