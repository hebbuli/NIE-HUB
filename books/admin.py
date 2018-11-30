from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Books)
admin.site.register(Book_details)
admin.site.register(Waiting_books)
admin.site.register(Transaction_books)


