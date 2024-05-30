from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import CustomUser


class CustomUserUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = UserCreationForm.Meta.fields + ("mobile",)


class CustomUserUserChangeForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = UserChangeForm.Meta.fields
        
