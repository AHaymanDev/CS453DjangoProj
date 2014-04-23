from django.db import models

# Create your models/tables here.
# ! Foreign keys go BELOW tables they reference !
          
          
class Book(models.Model):
    isbn = models.CharField(max_length=17,primary_key=True)
    title = models.CharField(max_length=40)
    author = models.CharField(max_length=40)
    category = models.CharField(max_length=40)
    #book_price = models.OneToOneField('Prices')

    def __unicode__(self):
        return self.isbn, self.title, self.author, self.category


class Prices(models.Model):
    isbn = models.ForeignKey(Book)
    price = models.IntegerField()

    def __unicode__(self):
        return self.isbn, self.price


class Cart(models.Model):
    username = models.CharField(max_length=15, primary_key=True)
    isbn = models.ForeignKey(Book) #models.CharField(max_length=17) # foreign key to book
    quantity = models.IntegerField(default=0)
    price = models.DecimalField(max_digits=5, decimal_places=2)

    def __unicode__(self):
        return self.username, self.isbn, self.quantity, self.price


class Returns(models.Model):
    username = models.CharField(max_length=15, primary_key=True) # foreign key to login
    isbn = models.ForeignKey(Book) #models.CharField(max_length=17) # foreign key to book
    #book = models.ManyToManyField(Book)
    returndate = models.DateField(auto_now=False, auto_now_add=False)

    def __unicode__(self):
        return self.username, self.isbn, self.returndate
