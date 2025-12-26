from rest_framework import serializers

class Author_Serializer(serializers.Serializer):
    id=serializers.IntegerField()
    name=serializers.CharField()
    country=serializers.CharField()

class Book_Serializer(serializers.Serializer):
    id=serializers.IntegerField()
    name=serializers.CharField()
    genre=serializers.CharField()
    author=Author_Serializer()