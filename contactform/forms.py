
"""
from django.forms import ModelForm
from contactform.models import Contact


class ContactForm(ModelForm):

    class Meta:
        model = Contact
        fields = ['subject', 'sender', 'message', 'copy']

"""


