from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as ua
from core import models
from django.utils.translation import gettext as _
# Register your models here.

class UserAdmin(ua):
    ordering = ['id']
    list_display = ['email', 'name']
    fieldsets = (
        (None, {'fields':('email', 'password')}),
        (_('personal_info'), {'fields':('name',)}),
        (_('permissions'), {'fields':('is_active', 'is_staff', 'is_superuser')}),
        (_('important_dates'), {'fields':('last_login',)})
    )
    add_fieldsets =(
        (None, {
            'classes':('wide',),
            'fields':('email','password1','password2')}),
    )

admin.site.register(models.User, UserAdmin)