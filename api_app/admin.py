from django.contrib import admin
from .models import Author, Book


# Register your models here.

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display=('name', 'id','country')
    list_filter=('country',)
    search_fields=['name', 'country']

@admin.register(Book)
class BooksAdmin(admin.ModelAdmin):
    list_display=['name', 'id', 'genre', 'author']
    list_filter=['genre', 'author']
    search_fields=['name', 'genre', 'author']
