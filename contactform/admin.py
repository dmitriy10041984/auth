
"""
from django.contrib import admin
from contactform.models import Contact

class ContactAdmin(admin.ModelAdmin):
    fields = ['subject', 'sender', 'message', 'copy']
    list_filter = ['subject']
    list_display = ('subject', 'sender', 'copy')
    search_fields = ['subject']

    class Media:
        js = (
            '/static/tiny_mce/tiny_mce.js',
            '/static/tiny_mce/tiny_mce_init.js',
        )


"""
