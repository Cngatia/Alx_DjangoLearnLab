~~~python 
# Import the Book model
>>> from bookshelf.models import book

# Create a Book instance with the title "1984", author "George Orwell", and publication year 1949.
Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
