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


