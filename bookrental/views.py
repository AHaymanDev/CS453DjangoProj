from django.shortcuts import render, render_to_response
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from bookrental.forms import UserCreateForm

# Create your views here.


def book(request):
    return render_to_response('bookrental/Books.html')


def checkout(request):
    return render_to_response('bookrental/Checkout.html')


def info(request):
    return render_to_response('bookrental/InfoPage.html')


def loginfunc(request):
    username = password = ''
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            state = "You've successfully logged in!"
    else:
        state = "Your username and/or password were incorrect."

    return render_to_response('bookrental/Login.html', {'state': state, 'username': username})


def return_confirm(request):
    return render_to_response('bookrental/ReturnConfirm.html')


def returns(request):
    return render_to_response('bookrental/Returns.html')


def warning(request):
    return render_to_response('bookrental/Warning.html')


def cart(request):
    return render_to_response('bookrental/YourCart.html')


def category(request):
    return render_to_response('bookrental/category.html')


def login_failure(request):
    return render_to_response('bookrental/login_failure.html')


# Register a new user with a custom form, log them in, and redirect
# to the Warning page.
def new_user(request):
    user_form = UserCreateForm(request.POST)
    if user_form.is_valid():
        username = user_form.clean_username()
        password = user_form.clean_password2()
        user_form.save()
        user = authenticate(username=username, password=password)
        login(request, user)
        return render_to_response('bookrental/new_user.html')# HttpResponseRedirect('Warning.html')
    return render(request, 'bookrental/new_user.html',
        {'user_form': user_form})     #'bookrental/new_user.html')


def update_user(request):
    return render_to_response('bookrental/update_user.html')
