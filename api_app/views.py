from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from rest_framework.decorators import api_view
from rest_framework.response import Response
from . models import Author, Book
from .serializers import Author_Serializer, Book_Serializer
# Create your views here.

@api_view(['GET'])
def date_time(request):
    now=datetime.now()
    return Response(now)

# @api_view(['GET'])
# def show_book(request):
    # books=Book.objects.all()
    # response=[]
    # for i in books:
    #     response.append({
    #         'id':i.id,
    #         'name':i.name,
    #         'author':{
    #             'id':i.author.id,
    #             'name':i.author.name,
    #             'country':i.author.country,
    #                 }
    #         })
    # return Response(response)

@api_view(['GET'])
def show_book(request):
    books=Book.objects.all()
    response=[]
    for book in books:
        response.append(Book_Serializer(book).data)
    return Response(response)

'''
{ "name" : "Guido Van Rossum" , "country" : "Germany" }
'''

@api_view(["post"])
def author_add(request):
    name=request.data.get('name')
    country=request.data.get('country')
    author=Author       (
        name = name,
        country =country )
    author.save()
    print(Author_Serializer((author)).data)
    return Response(Author_Serializer((author)).data)
