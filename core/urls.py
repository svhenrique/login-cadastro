
from django.urls import path, include
from .views import CadastroView, LogarView, IndexView
from django.views.generic.base import TemplateView

urlpatterns = [
    path('', IndexView.as_view(), name="index"),
    path('conta/', include('django.contrib.auth.urls')),  # rotas de atuenticação do próprio django,
    path('conta/cadastro/', CadastroView.as_view(), name="cadastro"),
    path('conta/login/', LogarView.as_view(), name="login"),
]
