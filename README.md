BookRental
==========

Django application to service as a computer science book rental system.


<b>SQL to Django Queries:</b>

<p>info page, displays the user's usersname and password</p>

<u>SQL:</u><br>
SELECT username, password<br>
FROM login<br>

<u>Django:</u><br>
Login.object.filter(username, password)

<p>Books page, displays a table of book titles</p>

<u>SQL:</u><br>
SELECT title<br>
FROM Book<br>

<u>Django:</u><br>
Book.object.filter(title)

<p>Login page, displays the name of the user</p>

<u>SQL:</u><br>
SELECT name<br>
FROM returns<br>
WHERE name = "John"<br>

<u>Django:</u><br>
Logins.object.filter(name_iexact="John")

<b>Returns page, gets the isbn that the user needs to return</b>

<u>SQL:</u><br>
SELECT isbn<br>
FROM returns, login<br>
WHERE returns.isbn = book.isbn <br>

<u>Django:</u><br>
Returns.object.filter(Login__book_isbn=1234)

<p>Returns page, displays table of user's username</p>

<u>SQL:</u><br>
SELECT username<br>
FROM returns, login<br>

<u>Django:</u><br>
Returns.object.filter(Login_username)


Display the current user's full name at the top of each page after logging in (ex. cart page).

<u>SQL:</u><br>
SELECT name<br>
FROM Cart

<u>Django:</u><br>
Cart.objects.get(name)

<b>On the cart page, display a table of the isbns, prices, and quantities of books a user wishes to checkout.</b>

<u>SQL:</u><br>
SELECT isbn, title, quantity, price<br>
FROM Cart, Book<br>
WHERE Cart.isbn = Book.isbn

<u>Django:</u><br>
Cart.objects.get(isbn)<br>
Cart.objects.get(book__isbn__title)<br>
Cart.objects.get(quantity)<br>
Cart.objects.get(price)

<b>On the checkout page, display the user's name, email, phone number, and returndate as a table.</b>

<u>SQL:</u><br>
SELECT username, name, email, phone, returndate<br>
FROM Returns, Login<br>
WHERE Returns.username = Login.username

<u>Django:</u><br>
Returns.objects.get(login__username__name)<br>
Returns.objects.get(login__username__email)<br>
Returns.objects.get(login__username__phone)<br>
Returns.objects.get(returndate)


<b>On the return page, display the user's name and email in addition to book titles, quantities, and the return date.</b>

<u>SQL:</u><br>
SELECT name, email, title, quantity, returndate<br>
FROM Login, Book, Cart, Returns<br>
WHERE Login.username = Returns.username<br>
  ^ Returns.isbn = Book.isbn<br>
  ^ Returns.username = Cart.username
  
<u>Django:</u><br>
Returns.objects.get(login__username__name)<br>
Returns.objects.get(login__username__email)<br>
Returns.objects.get(login__username__phone)<br>
Returns.objects.get(book__isbn__title)<br>
Returns.objects.get(cart__username__quantity)<br>
Returns.objects.get(returndate)

<b>On the books' info page, display the books' isbn, title, author, and category:</b>

<u>SQL:</u><br>
SELECT isbn,title,author,category<br>
FROM   Book,Categories<br>
WHERE Categories.category=Book.category<br>
      ^Book.isbn=''<br>
      ^Book.title=''<br>
      ^Book.author=''<br>

<u>Django:</u><br>
Book.objects.get(isbn__exact)<br>
Book.objects.get(title__exact)<br>
Book.objects.get(author__exact)<br>
Book.objects.get(categories__category__exact)<br>




<b>On the list of books page, display the books' author and title:</b>

<u>SQL:</u><br>
SELECT title,author<br>
FROM Book<br>
WHERE Book.title =' '<br>
      ^Book.author=' '<br>

<u>Django:</u><br>
Book.objects.get(title__exact)<br>

Book.objects.get(author__exact)<br>

<b>On the Categories Page, display all the categories:</b>

<u>SQL:</u><br>
SELECT category<br>
FROM Categories<br>

<u>Django:</u><br>
Category.objects.all()<br>

