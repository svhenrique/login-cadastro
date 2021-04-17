"""logincadastro URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView
from django.conf.urls.static import static
from django.conf import settings
from core.views import IndexView

import django.contrib.auth.urls
urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('admin/', admin.site.urls),
    path('conta/', include('django.contrib.auth.urls')),  # rotas de atuenticação do próprio django
    # ver se deve apagar as outras rotas que o django tem no auth.urls
    path('conta/', include('core.urls')),  # incluindo página de cadastro
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

