
from django.urls import path, include
from .views import CadastroView, LogarView, IndexView
from django.views.generic.base import TemplateView

urlpatterns = [
    path('', IndexView.as_view(), name="index"),
    path('conta/login/', LogarView.as_view(), name="login"), # deve-se colocar primeiro pois fica com prioridade e nao usa as rotas de mesmo nome do include abaixo
    path('conta/', include('django.contrib.auth.urls')),  # rotas de atuenticação do próprio django,
    path('conta/cadastro/', CadastroView.as_view(), name="cadastro"),
]
