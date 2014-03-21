BookRental
==========

Django application to service as a computer science book rental system.

<b>SQL to Django Queries:</b>

3. Display the current user's full name at the top of each page after logging in (ex. cart page).

<u>SQL:</u>
SELECT name
FROM Cart

<u>Django:</u>
Cart.objects.get(name)

4. <b>On the cart page, display a table of the isbns, prices, and quantities of books a user wishes to checkout.</b>

<u>SQL:</u>
SELECT isbn, title, quantity, price
FROM Cart, Book
WHERE Cart.isbn = Book.isbn

<u>Django:</u>
Cart.objects.get(isbn)
Cart.objects.get(book__isbn__title)
Cart.objects.get(quantity)
Cart.objects.get(price)

5. <b>On the checkout page, display the user's name, email, phone number, and returndate as a table.</b>

<u>SQL:</u>
SELECT username, name, email, phone, returndate
FROM Returns, Login
WHERE Returns.username = Login.username

<u>Django:</u>
Returns.objects.get(login__username__name)
Returns.objects.get(login__username__email)
Returns.objects.get(login__username__phone)
Returns.objects.get(returndate)


6. <b>On the return page, display the user's name and email in addition to book titles, quantities, and the return date.</b>

<u>SQL:</u>
SELECT name, email, title, quantity, returndate
FROM Login, Book, Cart, Returns
WHERE Login.username = Returns.username
  ^ Returns.isbn = Book.isbn
  ^ Returns.username = Cart.username
  
<u>Django:</u>
Returns.objects.get(login__username__name)
Returns.objects.get(login__username__email)
Returns.objects.get(login__username__phone)
Returns.objects.get(book__isbn__title)
Returns.objects.get(cart__username__quantity)
Returns.objects.get(returndate)
