from django.conf.urls import url, patterns, include
from django.contrib import admin

from superauthentication import views



urlpatterns = [
    url(r'^register/$', views.Registration.as_view()),
    url(r'^login/$', views.LoginFormView.as_view()),
    url(r'^logout/$', views.LogoutView.as_view()),
]

