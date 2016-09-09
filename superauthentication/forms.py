from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
from django import forms
from django.utils.translation import ugettext_lazy as _
from django.contrib import admin
from django import forms
from captcha.fields import CaptchaField



class UserCreationFormExtended(UserCreationForm):

    capcha = CaptchaField()

    def __init__(self, *args, **kwargs): 
        super(UserCreationFormExtended, self).__init__(*args, **kwargs) 
        self.fields['email'] = forms.EmailField(label=_("e-mail"), max_length=75)



