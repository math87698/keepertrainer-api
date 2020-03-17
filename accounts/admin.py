from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin
from django.utils.translation import ugettext_lazy as _
from rest_framework.authtoken.admin import TokenAdmin

from .models import User

TokenAdmin.raw_id_fields = ['user']

@admin.register(User)
class UserAdmin(DjangoUserAdmin):
    """ Define admin model for custom user model with no username field. """

    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
                                       'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2'),
        }),
    )
    list_display = ('email', 'first_name' , 'last_name', 'is_staff')
    search_fields = ('email', 'first_name' , 'last_name')
    ordering = ('email',)