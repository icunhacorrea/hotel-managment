from core.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

class UserCreateForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("email",)

class UserChangeForm(UserChangeForm):
    class Meta:
        model = User
        fields = ("email",)
