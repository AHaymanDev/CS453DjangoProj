from django.shortcuts import render, render_to_response
from django.http import HttpResponse

# Create your views here.

def book(request):
     return render_to_response('bookrental/Books.html')

def checkout(request):
     return render_to_response('bookrental/Checkout.html')

def info(request):
     return render_to_response('bookrental/InfoPage.html')

def login(request):
     return render_to_response('bookrental/Login.html')

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
     
def new_user(request):
     return render_to_response('bookrental/new_user.html')
     
def update_user(request):
     return render_to_response('bookrental/update_user.html')
