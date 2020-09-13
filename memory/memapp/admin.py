from django.contrib import admin
from .models import Person, Task
from django.contrib.auth.admin import UserAdmin


class PersonAdmin(UserAdmin):
    list_display = ('email', 'username', 'is_admin', 'is_staff', 'is_active')
    search_fields = ('email', 'username')

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()


admin.site.register(Person, PersonAdmin)
admin.site.register(Task)

