import sendgrid
import os
from sendgrid.helpers.mail import Mail, Email, To, Content

from decouple import config

class ApiClient:

    client = sendgrid.SendGridAPIClient(api_key=config('SENDGRID_API'))

    def get_client(self):
        return self.client

class MailMessage:

    from_email = ""  # Change to your verified sender
    to_email = ""  # Change to your recipient
    subject = ""
    content = ""

    def __init__(self, from_email, to_email, subject, content):
        if len(content) != 2:
            raise TypeError(f"__init__() content aceita apenas 2 parâmetros mas {len(content)} foram dados")
        self.from_email = Email(from_email)
        self.to_email = To(to_email)
        self.subject = subject
        self.content = Content(*content)

    def get_mail(self):
        return Mail(self.from_email, self.to_email, self.subject, self.content)

class Sender:

    client = ApiClient()
    mail = None

    def __init__(self, email):
        self.mail = MailMessage(*email)

    def send(self):
        try:
            client = self.client.get_client()
            response = client.send(self.mail.get_mail())
            return response.status_code
        except Exception as e:
            return e