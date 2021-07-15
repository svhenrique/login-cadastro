
from django.urls import path, include
from .views import CadastroView, LogarView, IndexView
from .forms import CustomPasswordResetForm
from django.views.generic.base import TemplateView
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', IndexView.as_view(), name="index"),

    path('conta/cadastro/', CadastroView.as_view(), name="cadastro"),

    path('conta/login/', LogarView.as_view(), name="login"),
    path('conta/logout/', auth_views.LogoutView.as_view(), name='logout'),

    path('conta/password_reset/', auth_views.PasswordResetView.as_view(form_class=CustomPasswordResetForm, template_name='password_reset.html'), name='password_reset'),
    path('conta/password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'), name='password_reset_done'),
    path('conta/reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'), name='password_reset_confirm'),
    path('conta/reset/complete/', auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'), name='password_reset_complete'),
]