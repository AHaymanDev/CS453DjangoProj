from django.shortcuts import render, render_to_response
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from bookrental.forms import UserCreateForm
from bookrental.models import Book
from bookrental.tables import BookTable
from django_tables2 import RequestConfig
from django.core.context_processors import csrf
from django.core.urlresolvers import reverse

# Create your views here.


def book(request):
    table = BookTable(Book.objects.all())
    RequestConfig(request).configure(table)
    return render_to_response('bookrental/Books.html', {'table': table})


def checkout(request):
    return render_to_response('bookrental/Checkout.html')


def info(request):
    return render_to_response('bookrental/InfoPage.html')


def login_page(request):
    c = {}
    c.update(csrf(request))
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect('warning/')
        else:
            return HttpResponseRedirect('login_failure/')
    return render_to_response('bookrental/Login.html', c)


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
    c = {}
    c.update(csrf(request))
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse('warning'))
    return render_to_response('bookrental/login_failure.html', c)


def logout_page(request):
    logout(request)
    return render(request, 'bookrental/Login.html')


# Register a new user with a custom form, log them in, and redirect to the Warning page.
def new_user(request):
    if request.method == 'POST':
        user_form = UserCreateForm(request.POST)
        if user_form.is_valid():
            username = user_form.clean_username()
            password = user_form.clean_password2()
            user_form.save()
            user = authenticate(username=username, password=password)
            login(request, user)
            return HttpResponseRedirect(reverse('warning'))
    user_form = UserCreateForm()
    return render(request, 'bookrental/new_user.html', {'user_form': user_form})


def update_user(request):
    return render_to_response('bookrental/update_user.html')
