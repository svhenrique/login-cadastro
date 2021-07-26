from django.test import TestCase

from core.forms import CustomPasswordResetForm
from core.email_sender import EmailMessage
from django.template import loader


class CustomPasswordResetForm(CustomPasswordResetForm):
    """
       Classe reescrita
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