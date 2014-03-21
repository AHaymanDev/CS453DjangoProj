from django.contrib import admin

# Register your models here.
# Allows one to add function from the models/SignUp
# to the admin site
from models import SignUp

class SignUpAdmin(admin.ModelAdmin):
    class Meta:
        model = SignUp
        
admin.site.register(SignUp, SignUpAdmin)
