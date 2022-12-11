from django.contrib import admin
from .models import Author,Editorial,Category,Books
# Register your models here.
admin.site.register([Author,Editorial,Category,Books])
