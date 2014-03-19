from django.db import models

# Create your models/tables here.
# ! Foreign keys go BELOW tables they reference !

class Login(models.Model):
     username = models.CharField(max_length=15, primary_key=True)
     password = models.CharField(max_length=15)
     name = models.CharField(max_length=15)
     email = models.CharField(max_length=40)
     phone = models.CharField(max_length=10)
     def __unicode__(self):
          return self.username, self.password
     def user_info(self):
          return self.name, self.email, self.phone

class Cart(models.Model):
     username = models.CharField(max_length=15, primary_key=True) # foreign key to login
     #poll = models.ForeignKey(Poll)
     isbn = models.CharField(max_length=17) # foreign key to book
     #poll = models.ForeignKey(Poll)
     quantity = models.IntegerField(default=0)
     price = models.DecimalField(max_digits=5, decimal_places=2)
     def __unicode__(self):
         return self.username, self.isbn, self.quantity, self.price

class Returns(models.Model):
     username = models.CharField(max_length=15, primary_key=True) # foreign key to login
     #poll = models.ForeignKey(Poll)
     isbn = models.CharField(max_length=17) # foreign key to book
     #poll = models.ForeignKey(Poll)
     returndate = models.DateField(auto_now=False, auto_now_add=False)
     def __unicode__(self):
     	 return self.username, self.isbn, self.returndate
     	 

