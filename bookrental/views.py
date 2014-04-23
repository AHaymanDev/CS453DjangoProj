from django.shortcuts import render, render_to_response
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.views.generic import ListView
from bookrental.forms import UserCreateForm
from bookrental.models import Book
from bookrental.tables import BookTable
from bookrental.models import Cart
from bookrental.tables import CartTable
from bookrental.models import Prices
from bookrental.tables import PriceTable
from django_tables2 import RequestConfig
from django.core.context_processors import csrf
from django.core.urlresolvers import reverse
from django.template import RequestContext
from django.db.models import F
from django.db.models import Q

# Create your views here.


def book(request):
    c = {}
    c.update(csrf(request))
    # select all the books with the user's current category selected
    select_books_from = request.POST.get('books')
    table = BookTable(Book.objects.filter(category=request.POST.get('books'))) # request.session['category']))
    RequestConfig(request).configure(table)
    if request.method == "GET":
        pks = request.POST.getlist("selection")
        selected_books = Book.objects.filter(pk__in=pks)

        kcart = None
        # put selected books in cart
        for b in selected_books:
            kcart = Cart(isbn=b.isbn, quantity=1)
            for p in Prices.objects.all():
                if b.isbn == p.isbn:
                    kcart.price = p.price
            kcart.save()

        # pass these books to cart page
        return HttpResponseRedirect(reverse('cart'), c, {'selected_books': selected_books})
    return render(request, 'bookrental/Books.html', {'table': table, 'select_books_from': select_books_from})


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
            # update session
            request.session['username'] = username1
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
    c = {}
    c.update(csrf(request))
    pks = request.GET.getlist("selection")

    # get new books to add, join with price table
    # TODO: works?
    new_cart = Cart.objects.all()
    #for c in new_cart:
    #    for p in pks:
    #        # if a cart item is not selected, delete it
    #        if c.isbn != p:
    #            c.delete()

    # merge current_cart with new_carts
    table = CartTable(new_cart)
    RequestConfig(request).configure(table)
    #if request.method == "POST":
    #    pks = request.POST.getlist("removed")
    #    # add all books NOT in removed
    #    removed_books = Cart.objects.filter(~Q(pk__in=pks))
    #    #pass these books to cart page as table
    #    table = removed_books
    #    RequestConfig(request).configure(table)
    #    return render(request, 'bookrental/YourCart.html', {'table': 'table'})
    return render(request, 'bookrental/YourCart.html', {'table': table})


def category(request):
    c = {}
    c.update(csrf(request))
    categories = {"programming_languages", "software_engineering", "computer_networking", "operating_systems", "database_systems", "computer_organization"}
    if request.method == 'POST':
        select_books_from = request.POST.get('books')
        request.session['category'] = select_books_from

        #select_books_from = None
        #for book_category in categories:
        #    if request.POST.get(book_category + ".x") is not None:
        #        select_books_from = book_category
        #        # change a user's current category
        #        request.session['category'] = select_books_from
        #        break
        return HttpResponseRedirect(reverse('book'), c, {'select_books_from': select_books_from})
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
            # update session
            request.session['username'] = username
            return HttpResponseRedirect(reverse('warning'))
    return render_to_response('bookrental/login_failure.html', c)


def logout_page(request):
    logout(request)
    # clear out cart
    for c in Cart.objects.all():
        c.delete()
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

            # update current session
            request.session['username'] = username1

            return HttpResponseRedirect(reverse('warning'))
    user_form = UserCreateForm()
    return render(request, 'bookrental/new_user.html', {'user_form': user_form})


def update_user(request):
    username = request.user.get_username()
    return render(request, 'bookrental/update_user.html', {'username': username})


################################################
