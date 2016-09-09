from django.conf.urls import url, patterns, include
from django.contrib import admin
from django.conf import settings


from ucaptcha import views

urlpatterns = [
    url(r'^$', views.home),

]


