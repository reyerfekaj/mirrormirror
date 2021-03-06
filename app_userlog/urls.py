"""project_base URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url
from .views import *

urlpatterns = [
    #url(r'^$', 'django.contrib.auth.views.login'),
    url(r'^$', login_page, name="login_page"),
    url(r'^logout/$', logout_page, name="logout_page"),
    # If user is not login it will redirect to login page
    #url(r'^accounts/login/$', 'django.contrib.auth.views.login'),
    url(r'^accounts/login/$', login_page, name="login_page"),
    url(r'^register/$', register, name="register"),
    url(r'^register/success/$', register_success, name="register_success"),    
    url(r'^home/$', home, name="home"),
    url(r'^info/$', info, name="info")
]
