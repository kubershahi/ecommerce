from django.contrib import admin

from django.contrib.auth.admin import UserAdmin
from user.models import User

class Useradmin(UserAdmin):
    list_display = ('email', 'username', 'first_name', 'last_name','date_joined', 'last_login', 'is_admin', 'is_staff', 'is_superuser')
    search_fields= ('email', 'username')
    readonly_fields = ('date_joined', 'last_login')

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

admin.site.register(User, Useradmin)