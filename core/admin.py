from django.contrib import admin
from .models import Book, BookCopy, BookCopyCondition, Event, Loan, Reader, Role, Publisher

admin.site.register([Book, BookCopy, BookCopyCondition, Event, Loan, Reader, Role, Publisher])