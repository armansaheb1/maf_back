from django.contrib import admin
from .models import CustomUser
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserUserChangeForm, CustomUserUserCreationForm


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserUserCreationForm
    fomr = CustomUserUserChangeForm
    model = CustomUser
    list_display = ["username", "email", "mobile", "is_staff"]
    fieldsets = UserAdmin.fieldsets + ((None, {"fields": ("mobile",)}),)
    add_fieldsets = UserAdmin.add_fieldsets + ((None, {"fields": ("mobile",)}),)


# Register your models here.
admin.site.register(CustomUser, CustomUserAdmin)
