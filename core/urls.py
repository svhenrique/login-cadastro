
from django.urls import path, include
from .views import CadastroView
from django.views.generic.base import TemplateView

urlpatterns = [
    path('cadastro/', CadastroView.as_view(), name="cadastro"),
]