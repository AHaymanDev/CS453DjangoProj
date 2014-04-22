from django.shortcuts import render, render_to_response
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.views.generic import ListView
from bookrental.forms import UserCreateForm
from bookrental.models import Login
from bookrental.models import Book
from bookrental.tables import BookTable
from django_tables2 import RequestConfig
from django.core.context_processors import csrf
from django.core.urlresolvers import reverse
from django.template import RequestContext

# Create your views here.


def book(request):

    # select all the books with the user's current category selected
    l = Login.objects.get(username=request.POST.get('username'))
    table = BookTable(Book.objects.filter(category=l.category))
    RequestConfig(request).configure(table)
    return render(request, 'bookrental/Books.html', {'table': table})


def checkout(request):
    return render_to_response('bookrental/Checkout.html')


def info(request):
    return render_to_response('bookrental/InfoPage.html')


def login_page(request):
    c = {}
    c.update(csrf(request))
    if request.method == 'POST':
        username1 = request.POST.get('username')
        password1 = request.POST.get('password')
        user = authenticate(username=username1, password=password1)
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
    c = {}
    c.update(csrf(request))
    categories = {"software_development", "programming_languages", "software_engineering", "computer_networking", "operating_systems", "database_systems", "computer_organization"}
    if request.method == 'POST':
        select_books_from = None
        for book_category in categories:
            if request.POST.get(book_category) is not None:
                select_books_from = book_category
                # change a user's current category
                l = Login.objects.get(username=request.POST.get('username'))
                l.category = select_books_from
                l.save()
                break
        return HttpResponseRedirect(reverse('book'), c, {'select_books': select_books_from})
    return render_to_response('bookrental/category.html', c, context_instance=RequestContext(request))


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
            username1 = user_form.clean_username()
            password = user_form.clean_password2()
            user_form.save()
            user = authenticate(username=username1, password=password)
            login(request, user)

            # update login database
            l = Login(username=username1, name=request.POST.get('first_name') + " " + request.POST.get('last_name'),
                      email=request.POST.get('email'))
            l.save()

            return HttpResponseRedirect(reverse('warning'))
    user_form = UserCreateForm()
    return render(request, 'bookrental/new_user.html', {'user_form': user_form})


def update_user(request):
    username = request.user.get_username()
    return render(request, 'bookrental/update_user.html', {'username': username})


################################################

class CategoryBooksList(ListView):
    template_name = 'bookrental/Books.html'
    context_object_name = 'category_books_list'

    def get_queryset(self):
        return Book.objects.filter()