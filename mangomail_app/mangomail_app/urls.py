"""
URL configuration for mangomail_app project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path
from mail_app import views
from mail_app.views import Create_newsletter

from django.views.generic import TemplateView
from mail_app.views import SubSuccess
from mail_app.views import NewsletterSuccess
from mail_app.views import SendNewsletterView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('subscribe/', views.subscribe, name='subscribe'),
    path('create-newsletter/', Create_newsletter, name='create_newsletter'),
    path('SubSuccess/', views.SubSuccess, name='SubSuccess'),
    path('NewsletterSuccess/', views.NewsletterSuccess, name='NewsletterSuccess'),
    path('send-newsletter/<int:newsletter_id>/', SendNewsletterView, name='sed_newsletter'), 
    path('send-newsletter/', views.SendNewsletterView, name='send_newsletter'),


]
