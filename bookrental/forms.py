__author__ = 'vagrant'
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

# Extending Django's UserCreateForm to include name, email, and phone
# along with username, password, and password confirmation.


class UserCreateForm(UserCreationForm):
    fullname = forms.CharField()
    email = forms.EmailField()
    phone = forms.CharField()

    #class Meta:
    #    model = User
    #    fields = ( "username") #, "password" )