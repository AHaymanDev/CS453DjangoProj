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
    phone = forms.CharField()

    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'password2')

    def save(self, commit=True):
        user = super(UserCreateForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        user.first_name = self.cleaned['first_name']
        user.last_name = self.cleaned['last_name']
        user.phone = self.cleaned_data['phone']

        if commit:
            user.save()
        return user