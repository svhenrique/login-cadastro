from django.shortcuts import redirect
from django.urls import reverse_lazy
from .forms import CustomUsuarioCreateForm, CustomLoginForm
from django.views.generic import FormView, TemplateView
from django.contrib.auth.views import LoginView

"""
Criar class based view para página de registro e deixar página vinculada ao admin
quieto

link para ajuda: https://www.youtube.com/watch?v=Ev5xgwndmfc&feature=emb_title
"""

class IndexView(TemplateView):

    template_name = 'index.html'

    def get(self, request, *args, **kwargs):
        if request.user.is_anonymous:
            return redirect('login')
        return super(IndexView, self).get(request, *args, **kwargs)


class CadastroView(FormView):

    template_name = 'cadastro.html'
    form_class = CustomUsuarioCreateForm
    success_url = reverse_lazy('index')

    def get(self, request, *args, **kwargs):
        if request.user.is_anonymous:
            return super(CadastroView, self).get(request, *args, **kwargs)
        return redirect('index')

    def form_valid(self, form, *args, **kwargs):
        # ver como desconectar usuário que estava conectado antes de cadastrar
        # e conectar usuario do cadastro
        form.save()
        return super(CadastroView, self).form_valid(form)

    def form_invalid(self, form, *args, **kwargs):
        return super(CadastroView, self).form_invalid(form)

class LogarView(LoginView):

    template_name = 'login.html'
    form_class = CustomLoginForm

    # nao e necessario por o success_url pois ja existe uma rota de redirecionamento
    # chamada LOGIN_REDIRECT_URL em settings.py

class SucessoView(TemplateView):

    template_name = 'sucesso.html'