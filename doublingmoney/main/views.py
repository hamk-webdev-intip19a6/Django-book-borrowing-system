from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
#from django.views import generic
from django.views.generic import (
    ListView,
    #DetailView,
    #CreateView,
    #UpdateView,
    #DeleteView
)
from django.db.models import Count, Q, OuterRef, Subquery, Value
from django.db.models.functions import Concat
from .models import Book, Inventory, Author


class HomeView(ListView):
    template_name = 'main/home.html'
    context_object_name = "available_book_list"

    def get_queryset(self):
        # returns list of available books.IF many of the same book add copies count
        q = Book.objects.filter(inventory__available=True).annotate(copies=Count('title'))
        return q

class SearchResultView(ListView):
    template_name = 'main/search_results.html'
    context_object_name = "book_list"

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            book_list = Book.objects.filter(
                Q(title__icontains=query) 
               # | Q(book_author__author_id__first_name__icontains=query)
               # | Q(book_author__author_id__last_name__icontains=query)
            ).annotate(copies=Count('inventory__available'))
        else:
            book_list = Book.objects.all().annotate(copies=Count('inventory__available'))
        return book_list

def book(request, book):
    book = book
    book_title = Book.objects.filter(title = book)
    available = Book.objects.filter(inventory__available=True, title=book).annotate(copies=Count('title'))
    context = {'book_title': book_title, 
                'available': available}
                
    return render(request, 'main/book.html', context)

def about(request):
    return render(request, 'main/about.html', {'title': 'About'})