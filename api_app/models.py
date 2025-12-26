from django.db import models

# Create your models here.

class Author(models.Model):
    name=models.CharField(max_length=30, blank=True)
    country=models.CharField(max_length=15, blank=True)
    def __str__(self):
        return self.name

class Book(models.Model):
    name=models.CharField(max_length=30, blank=True)
    genre=models.CharField(max_length=15, blank=True)
    author=models.ForeignKey(Author, on_delete=models.CASCADE)
    def __str__(self):
        return self.name