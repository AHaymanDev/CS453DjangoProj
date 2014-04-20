__author__ = 'vagrant'
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

# Extending Django's UserCreateForm to include name, email, and phone
# along with username, password, and password confirmation.


class UserCreateForm(UserCreationForm):
    first_name = forms.CharField()
    last_name = forms.CharField()
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ('username', 'password', 'password2', 'email')

    def save(self, commit=True):
        user = super(UserCreateForm, self).save(commit=False)
        user.email = self.cleaned_data['email']

        if commit:
            user.save()
        return user