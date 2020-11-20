from django.http import HttpResponse
from django.shortcuts import render
from books.models import Book

# Create your views here.


def index(request):
    return HttpResponse("Hello, \
                        world. You're at the' \
                        books index")


def latest_books(request):
    book_list=Book.objects.order_by("-publication_date")[:10]
    return render(request,'latest_books.html',{'book_list':book_list})
