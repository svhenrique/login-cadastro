import sendgrid
from sendgrid.helpers.mail import Mail, Email, To, Content

from decouple import config

EMAIL = config('EMAIL')

class ApiClient:

    _client = sendgrid.SendGridAPIClient(api_key=config('SENDGRID_API'))

    def get_client(self):
        return self._client

class EmailMessage:

    client = ApiClient()
    from_email = EMAIL  # email authenticated in sendgrid
    to_email = None  # Recipient of the message
    subject = None  # Subject of the message
    content = None  # Tuple with MIME type and content

    def __init__(self, to_email, subject, content):
        if len(content) != 2:
            raise TypeError(f"__init__() content aceita apenas 2 parâmetros mas {len(content)} foram dados")
        self.to_email = To(to_email)
        self.subject = subject
        self.content = Content(*content)

    def _get_mail(self):
        return Mail(self.from_email, self.to_email, self.subject, self.content)

    def send_email(self):
        try:
            client = self.client.get_client()
            message = self._get_mail()
            response = client.send(message)
            return response.status_code
        except Exception as e:
            return e
