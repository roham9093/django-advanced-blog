from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User,Profile

class CustomUserAdmin(UserAdmin):
    '''
    show the table of accounts model in Data Base
    '''
    model = User
    list_display = ('email', 'is_active', 'is_superuser')
    list_filter = ('email', 'is_active', 'is_superuser')
    search_fields = ('email',)
    ordering = ('email',)
    fieldsets = (
        ('Authentications', {
            "fields": (
                'email','password'
            ),
        }),
        ('Permissions', {
            "fields": (
                'is_staff','is_active','is_superuser'
            ),
        }),
        ('Group Permissions', {
            "fields": (
                'groups','user_permissions'
            ),
        }),
        ('Important Dates', {
            "fields": (
                'last_login',
            ),
        }),        
    )
    add_fieldsets = (
        ('new', {
            'classes':('wide',),
            'fields': (
                'email','password1','password2','is_staff','is_active','is_superuser'
            ),
        }),
    )
    

admin.site.register(Profile)
admin.site.register(User,CustomUserAdmin)    