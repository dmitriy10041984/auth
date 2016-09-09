from django.conf.urls import url, patterns, include
from django.contrib import admin

from contactform import views

urlpatterns = [
    url(r'^contact/', views.contactView),


]