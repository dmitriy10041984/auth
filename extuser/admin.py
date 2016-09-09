from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group
from .forms import UserChangeForm
from .forms import UserCreationForm
from .models import ExtUser


class UserAdmin(UserAdmin):
    """
    Base admin classs.
    form - form for change user settings.
    add_form - used for create users
    """
    form = UserChangeForm
    add_form = UserCreationForm

    # Fields listed in admin panel
    list_display = [
        'login',
        'email',
        'firstname',
        'middlename',
        'lastname',
        'date_of_birth',
        'is_admin',
        'bit',
        'avatar'


    ]

    # Filter for admin panel
    list_filter = ('is_admin',)

    # Fieldsets for ordering and grouping
    fieldsets = (
                (None, {'fields': ('login', 'email', 'password')}),
                ('Personal info', {
                 'fields': (
                     'firstname',
                     'middlename',
                     'lastname',
                     'avatar',
                     'date_of_birth',
                     'phone',
                     'foto',
                     'video',
                     'about',
                 )}),
                ('Permissions', {'fields': ('is_admin', 'is_active')}),
                ('Important dates', {'fields': ('last_login',)}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (
                'date_of_birth',
                'email',
                'password1',
                'password2'
            )}
         ),
    )

    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = ()

# Register ExtUser admin panel in Django
admin.site.register(ExtUser, UserAdmin)
admin.site.unregister(Group)