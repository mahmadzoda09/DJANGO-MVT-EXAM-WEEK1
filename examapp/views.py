from django.shortcuts import render , redirect
from .models import *

def main(request):
    return render(request,'main.html')

def author(request):
    authors = Author.objects.all()
    return render(request,'author.html',{'authors':authors})

def create(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        birth_date = request.POST.get('birth_date')
        
        Author.objects.create(first_name = first_name , last_name = last_name , birth_date = birth_date)
        
        return redirect('author')
    return render(request,'create.html')

def book(request):
    books = Book.objects.all()
    return render(request,'book.html',{'books':books})

def detail(request,id):
    book = Book.objects.get(id=id)
    return render(request,'detail.html',{'book':book})

def add(request):
    authors = Author.objects.all()
    if request.method == 'POST':
        title = request.POST.get('title')
        pages = request.POST.get('pages')
        price = request.POST.get('price')
        description = request.POST.get('description')
        author_id = request.POST.get('author')
        author = Author.objects.get(id = author_id)
        
        Book.objects.create(title=title,pages=pages,price=price,description=description,author=author)
        return redirect('book')
    
    return render(request,'add.html',{'authors':authors})

def delete(request,id):
    book = Book.objects.get(id=id)
    book.delete()
    return redirect('book')

def update(request,id):
    authors = Author.objects.all()
    book = Book.objects.get(id=id)
    if request.method == 'POST':
        new_title = request.POST.get('title')
        new_pages = request.POST.get('pages')
        new_price = request.POST.get('price')
        new_description = request.POST.get('description')
        author_id = request.POST.get('author')
        new_author = Author.objects.get(id = author_id)
        
        book.title = new_title
        book.pages = new_pages
        book.pages = new_pages
        book.description = new_description
        book.author = new_author
        
        book.save()
        return redirect('book')
    
    return render(request,'update.html',{'authors':authors,'book':book})