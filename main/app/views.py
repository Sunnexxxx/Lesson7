from django.shortcuts import render
from django.http import HttpResponse
from .models import Author, Book, Reader


# def index_views(request):
#     author = Author.objects.get(pk=3)
#     # books = Book.objects.filter(author=author)
#     book = author.book_set.all()
#     reader = Reader.objects.get(pk=1)
#     l_books = reader.liked_books.all()
#     book = author.book_set.get(pk=1)
#     l_readers = book.reader_set.all()
#     print(l_readers)
#     return HttpResponse("test")

def book_list_view(request):
    books = Book.objects.all()
    context = {'books': books}
    return render(request, 'main/book_list.html', context)


def book_details_view(request, book_slug):
    book = Book.objects.get(slug=book_slug)
    context = {"book": book}
    return render(request, "main/book_details.html", context)
