from django.shortcuts import render, redirect
from .models import Book
from django.http import HttpResponse

def book_list(request):
    books = Book.objects.all()
    return render(request, 'library/book_list.html', {'books': books})

def add_book(request):
    if request.method == "POST":
        title = request.POST["title"]
        author = request.POST["author"]
        isbn = request.POST["isbn"]
        Book.objects.create(title=title, author=author, isbn=isbn)
        return redirect("book_list")
    return render(request, 'library/add_book.html')