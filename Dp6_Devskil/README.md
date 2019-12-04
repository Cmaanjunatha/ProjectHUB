
# Books CRUD Application

## Introduction

This application uses Python 3 and Django 1.10. It contains a `Books` module for managing book entities.

## Problem statement

Your task is to implement four class-based views (CBV) and mixins to ensure that all unit tests pass. Please do not edit any templates, but use *Django messages framework* for success/error messages instead.

1. Implement `BookDetailView`. It should load book details for a given `ISBN` parameter. If the requested book doesn't exist, user should be redirected to `/books/` default route (`BookListView`: `books:index`).

2. Implement `BookCreateView`. It should populate a form field with book details. After successful submission, user should be redirected to the page of the created book (`BookDetailView`: `books:detail`). Please do not forget to add a validator to check the `ISBN`. The `ISBN` can be divided into parts with hyphens, that is it may only contain digits and hyphens. Validation can be done in the `Book` model. Additionally, please add the following messages:
   * `The book has been successfully created!` - when a book is added.
   * `The creation has failed.` - when the process of adding a book failed.

3. Implement `BookUpdateView`. It should populate form fields with book details for the passed `ISBN` parameter. If the book with a given `ISBN` doesn't exist, user should be redirected to `/books/` default route (`BookListView`: `books:index`). After successful submission, user should be redirected to the page showing the details of the edited book (`BookDetailView`: `books:detail`). Additionally, please add the following messages:
   * `The book has been successfully updated!` - when a book is updated.
   * `The update has failed.` - when the process of updating a book failed.

4. Implement `BookDeleteView`. It should delete a book with a given `ISBN` parameter. If the book with a given `ISBN` doesn't exist, user should be redirected to `/books/` default route (`BookListView`: `books:index`).  Once the book is deleted, user should be redirected to a list of books (`BookListView`: `books:index`). Additionally, please add the following messages:
   * `The book has been successfully deleted!` - when a book is deleted.
   * `The deletion has failed.` - when the process of deleting a book failed.

## Hints

Please **do not** modify unit tests.

## Setup

To execute the unit tests, use:

```
pip install -q -e . && python setup.py nosetests
```
