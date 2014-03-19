from django.db import models

# Create your models/tables here.
# ! Foreign keys go BELOW tables they reference !

class Cart(models.Model):
     username = models.CharField(max_length=15, primary_key=True) # foreign key to login
     isbn = models.CharField(max_length=17) # foreign key to book
     quantity = models.IntegerField(default=0)
     price = models.DecimalField(max_digits=5, decimal_places=2)
     def __unicode__(self):
         return self.username, self.isbn, self.quantity, self.price

class Returns(models.Model):
     username = models.CharField(max_length=15, primary_key=True) # foreign key to login
     isbn = models.CharField(max_length=17) # foreign key to book
     returndate = models.DateField(auto_now=False, auto_now_add=False)
     #poll = models.ForeignKey(Poll)
     def __unicode__(self):
     	 return self.username, self.isbn, self.returndate