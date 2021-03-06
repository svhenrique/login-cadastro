
from django.urls import path, include
from .views import RegisterView, IndexView, ActivateView
from .forms import CustomPasswordResetForm
from django.views.generic.base import TemplateView
from django.contrib.auth import views as auth_views
from .forms import CustomLoginForm

urlpatterns = [
    path('', IndexView.as_view(), name="index"),

    path('conta/cadastro/', RegisterView.as_view(), name="register"),
    path('conta/cadastro/success', TemplateView.as_view(template_name='success.html'), name="success"),
    path('conta/cadastro/failure', TemplateView.as_view(template_name='failure.html'), name="failure"),

    path('conta/login/', auth_views.LoginView.as_view(template_name='login.html', form_class=CustomLoginForm), name="login"),
    path('conta/logout/', auth_views.LogoutView.as_view(), name='logout'),

    path('conta/cadastro/<uidb64>/<token>/', ActivateView.as_view(), name='activate'),
    path('conta/password_reset/', auth_views.PasswordResetView.as_view(form_class=CustomPasswordResetForm, template_name='password_reset.html'), name='password_reset'),
    path('conta/password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'), name='password_reset_done'),
    path('conta/reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'), name='password_reset_confirm'),
    path('conta/reset/complete/', auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'), name='password_reset_complete'),
]
