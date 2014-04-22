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
from bookrental.models import Returns
from bookrental.tables import ReturnTable

# Create your views here.


def book(request):
    c = {}
    c.update(csrf(request))
    # select all the books with the user's current category selected
    select_books_from = request.POST.get('books')
    table = BookTable(Book.objects.filter(category=request.POST.get('books'))) # request.session['category']))
    RequestConfig(request).configure(table)
    if request.method == "GET":
        #pks = request.POST.getlist("selection")
        pks = request.GET.getlist("selection")
        selected_books = Book.objects.filter(pk__in=pks)

        # put selected books in cart
        # TODO: Doesn't work; not saving to the cart table!!!
        #for p in pks:
        kcart = Cart(isbn='978-123456', quantity=1, price=0)
            #for p in Prices.objects.all():
            #    if b.isbn == p.isbn:
            #        kcart.price = p.price
            #        break
        kcart.save()
        #table = CartTable(Cart.objects.all())))))
        #RequestConfig(request).configure(table)

        # pass these books to cart page
        return HttpResponseRedirect(reverse('cart'))#, c, {'table': table})
    return render(request, 'bookrental/Books.html', {'table': table, 'select_books_from': select_books_from})


def checkout(request):
    # displays a successful checkout page
    return render_to_response('bookrental/Checkout.html')


def info(request):
    return render_to_response('bookrental/InfoPage.html')


def login_page(request):
    c = {}
    c.update(csrf(request))
    if request.method == 'POST':
        # if the login button was clicked, authenticate the given user/pass combo
        username1 = request.POST.get('username')
        password1 = request.POST.get('password')
        user = authenticate(username=username1, password=password1)
        if user is not None:
            login(request, user)
            # update session
            request.session['username'] = username1
            # good login, so go to warning page
            return HttpResponseRedirect('warning/')
        else:
            # bad login, so go to failure
            return HttpResponseRedirect('login_failure/')
    return render_to_response('bookrental/Login.html', c)


def return_confirm(request):
    # display a return confirmation page
    return render_to_response('bookrental/ReturnConfirm.html')


def returns(request):
    c = {}
    c.update(csrf(request))
    # Create a table of all returnable objects
    table = ReturnTable(Returns.objects.all())
    RequestConfig(request).configure(table)
    if request.method == "POST":
        # get list of returning books, delete from total returns
        pks = request.POST.getlist("returning")
        returned_books = Returns.objects.filter(~Q(pk__in=pks))
        # pass these books to return confirmation page as table
        table = ReturnTable(returned_books)
        RequestConfig(request).configure(table)
        return render(request, 'bookrental/ReturnConfirm.html', {'table': 'table'})
    return render(request, 'bookrental/Returns.html', {'table': table})


def warning(request):
    # displays the disclaimer page
    return render_to_response('bookrental/Warning.html')


def cart(request):
    c = {}
    c.update(csrf(request))
    pks = request.GET.getlist("selection")

    # get new books to add, join with price table
    new_cart = Cart.objects.all()
    for c in new_cart:
        for p in pks:
            # if a cart item is not selected, delete it
            if c.isbn != p:
                c.delete()

    table = CartTable(new_cart)
    RequestConfig(request).configure(table)
    if request.method == "POST":
        pks = request.POST.getlist("removed")
        # add all books NOT in removed
        removed_books = Cart.objects.filter(~Q(pk__in=pks))
        #pass these books to cart page as table
        table = CartTable(removed_books)
        RequestConfig(request).configure(table)
        # display updated table on same page
        return render(request, 'bookrental/YourCart.html', {'table': 'table'})
    return render(request, 'bookrental/YourCart.html', {'table': table})


def category(request):
    c = {}
    c.update(csrf(request))
    # all available categories for books
    categories = {"programming_languages", "software_engineering", "computer_networking", "operating_systems", "database_systems", "computer_organization"}
    if request.method == 'POST':
        # if the button was pressed, pass the selected category to the books page
        select_books_from = request.POST.get('books')
        request.session['category'] = select_books_from
        return HttpResponseRedirect(reverse('book'), c, {'select_books_from': select_books_from})
    return render_to_response('bookrental/category.html', c, context_instance=RequestContext(request))


def login_failure(request):
    c = {}
    c.update(csrf(request))
    if request.method == 'POST':
        # if the button was clicked, authenticate user and pass in auth_user table
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            # if the user/pass pair is good, login and redirect to warning page
            login(request, user)
            # update session
            request.session['username'] = username
            return HttpResponseRedirect(reverse('warning'))
    return render_to_response('bookrental/login_failure.html', c)


def logout_page(request):
    # clear out their cart
    for c in Cart.objects.all():
        c.delete()
    # logout the user
    logout(request)
    # go back to the login page
    return render(request, 'bookrental/Login.html')


# Register a new user with a custom form, log them in, and redirect to the Warning page.
def new_user(request):
    if request.method == 'POST':
        # when they hit submit, check if their form is correct
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
    if request.method == 'POST':
        # if they hit submit, get their user and pass
        username = request.user
        password = request.POST.get('password')
        # Current password is correct, so can set new password
        if authenticate(username=username, passoword=password) is not None:
            request.user.set_password(request.POST.get('new_password'))
        request.user.email = request.POST.get('email')
        # go to category page
        return HttpResponseRedirect(reverse('category'))
    return render_to_response('bookrental/update_user.html')


################################################
