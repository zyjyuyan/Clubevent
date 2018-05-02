"""Clubevent URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.conf.urls import url, include  # Django 1.x
from django.urls import path, re_path  # Django 2.0
from django.contrib.auth import views as auth_views

import main.views.index
import main.views.user


urlpatterns = [
    path('admin/', admin.site.urls),
    # index
    re_path(r'^$', main.views.index.index, name='index'),
    url(r'^user/signup$', main.views.user.userSignup),  # POST
    url(r'^user/signin$', auth_views.LoginView.as_view(template_name='user/signin.html'), name='login'),  # POST
    url(r'^user/signout$', auth_views.LogoutView.as_view(), name='logout'),
]
