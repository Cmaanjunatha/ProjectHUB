# -*- coding: utf-8 -*-

"""Books views."""

from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib import messages
from django.shortcuts import redirect
from django.http import Http404
from django.urls import reverse_lazy

from .models import Book


class BookListView(ListView):
    """Show all books."""

    model = Book


class BookDetailView:
    """Show the requested book."""


class BookCreateView:
    """Create a new book."""


class BookUpdateView:
    """Update the requested book."""


class BookDeleteView:
    """Delete the requested book."""
