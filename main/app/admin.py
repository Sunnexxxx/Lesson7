from django.contrib import admin
from .models import Author, Book, TestTable, Ticket, Reader


admin.site.register(Author)
admin.site.register(Book)
admin.site.register(TestTable)
admin.site.register(Ticket)
admin.site.register(Reader)