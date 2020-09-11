from django.contrib import admin
from .models import Person
from django.contrib.auth.admin import UserAdmin


class PersonAdmin(UserAdmin):
    list_display = ('email', 'username', 'is_admin', 'is_staff')
    search_fields = ('email', 'username')

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()


admin.site.register(Person, PersonAdmin)

