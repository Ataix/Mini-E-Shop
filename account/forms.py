from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms

ShopUser = get_user_model()


class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = ShopUser
        fields = ('email', 'password1', 'password2')

    def save(self):
        email = self.cleaned_data.get('email')
        password = self.cleaned_data.get('password1')
        user = get_user_model().object.create_user(email=email, password=password)
        return user


class UserModifyForm(UserChangeForm):
    class Meta:
        model = ShopUser
        fields = ('last_name', 'first_name', 'bio')
