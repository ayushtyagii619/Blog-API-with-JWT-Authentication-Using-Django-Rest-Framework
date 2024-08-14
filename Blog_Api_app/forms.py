from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields  = ("email",)

class CustomuserChnageForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ("email",)