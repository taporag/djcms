from django.contrib.auth.forms import UserChangeForm
from .models import User

class CustomUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = User