from django import forms

from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm, UsernameField

from django.utils.translation import gettext, gettext_lazy as _

from .models import CustomUsuario, UsuarioManager

class CustomLoginForm(AuthenticationForm):

    password = forms.CharField(
        label=_("Password"),
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'current-password'}),
    )

    username = UsernameField(widget=forms.TextInput(attrs={'autofocus': True, 'type': 'email'}))
    password.widget.attrs.update({'autocomplete': 'off'})


class CustomUsuarioCreateForm(UserCreationForm):
    """
    Formulario para criar usuarios

    Importante:
        Os usuarios criados pelo forms nao serao staffs ou superusers pois a criacao atraves do formulario
        esta usando o metodo create_user de UsuarioManager, ou seja, so podem acessar a pagina de login.
        Entretanto, superusers criados pelo comando creatsuperusers de manage.py sera staff e superuser,
        alem de poder acessar a pagina de login.
    """
    imagem = forms.FileField(required=False)
    username = forms.EmailField(required=True)

    class Meta:
        model = CustomUsuario
        fields = ('username', 'first_name', 'last_name', 'imagem')
        labels = {'username': 'E-mail'}

    def save(self, commit=True):

        user = CustomUsuario.objects.create_user(
            self.cleaned_data['username'],
            self.cleaned_data['password1'],
            imagem=self.cleaned_data['imagem'],
            first_name=self.cleaned_data['first_name'],
            last_name=self.cleaned_data['last_name']
        )

class CustomUsuarioChangeForm(UserChangeForm):
    """
    Formulario para modificar usuarios
    """
    class Meta:
        model = CustomUsuario
        fields = ('first_name', 'last_name', 'imagem')
