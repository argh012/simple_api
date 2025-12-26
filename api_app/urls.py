from django.urls import path
from . import views

urlpatterns = [
    path("date/", views.date_time),
    path('books/get', views.show_book),
    path('author/add', views.author_add)
]
