from django.shortcuts import render
from django.shortcuts import HttpResponse
from .models import Book
import datetime

# Create your views here.
def index(request):
    return HttpResponse('Hello World')

def addBook(request):
    ch1 = Book(name = "ME", pageNumber = 32, genre = "Action", publishDate = '2014-03-12')
    ch1.save()
    return HttpResponse("Added a new Book")

def all(request):
    book1 = Book.objects.all()
    for each in book1:
        print(each)
    return HttpResponse("Printing Books")

def after(request):
    book1 = Book.objects.all()
    for each in book1:
        if(each.publishDate >= datetime.date(2018,1,1)):
            print(each)
        else:
            print("")
    return HttpResponse("Only After 2017")

def change(request):
    book1 = Book.objects.all()
    for each in book1:
        if(each.publishDate >= datetime.date(2018,1,1)):
            each.genre = "Fiction"
            print(each)
        else:
            print(each)
    return HttpResponse("Changing")