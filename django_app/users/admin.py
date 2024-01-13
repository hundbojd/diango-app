from django.contrib import admin
from django.contrib.auth.models import Group, User
from .models import Profile

admin.site.unregister(Group)


class ProfileInLine(admin.StackedInline):
    model = Profile


class UserAdmin(admin.ModelAdmin):
    model = User
    fields = ["username", "first_name", "last_name", "email", "last_login", "is_staff", "user_permissions", "date_joined"]
    inlines = [ProfileInLine]


admin.site.unregister(User)
admin.site.register(User, UserAdmin)




