from rest_framework import serializers
from .models import Book,Author
from datetime import date

class Bookserializer(serializers.Modelserializer):
    class Meta:
        model = Book
        fields = ("title","publication_year","author")
    def validate_publication_year(self, value):
        current_year = date.today().year
        if value > current_year:
            raise serializers.ValidationError("Publication year cannot be in the future")
        return value
    

class Authorserializer(serializers.Modelserializer):
    book = Bookserializer(many =True, read_only = True)
    class Meta:
        model = Author
        fields = ("name","book")

        """
        Created serializers for the models.
        """

