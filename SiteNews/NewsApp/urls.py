"""SiteNews URL Configuration

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
from django.urls import path
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.conf import settings
from .views import index, base, post_details ,basetest,about ,contact,travel,health,video,divers,bisness,politic
admin.site.site_header ='    صـــحيفـــةالكليــــة الجامعيـــة  بالـخـرمــة'

urlpatterns = [

    path('', index, name='index'),
    path('basetest', basetest, name='basetest'),
    path('about', about, name='about'),
    path('post_details/<int:id>', post_details, name='post_details'),
    path('template', base, name='base'),
    path('contact', contact, name='contact'),
    path('travel', travel, name='travel'),
    path('health', health, name='health'),
    path('video', video, name='video'),
    path('divers', divers, name='divers'),
    path('bisness', bisness, name='bisness'),
    path('politic', politic, name='politic'),

]

