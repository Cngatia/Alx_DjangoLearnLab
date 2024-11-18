~~~ python
#Importing the Book model from the bookshelf app
>>> from bookshelf.models import Book

#Retrieving the specific book instance by title
>>> new_book = Book.objects.get(title='1984')

#Displaying book attributes
>>> new_book.title
    # Expected Output: '1984'

>>> new_book.author
    # Expected Output: 'George Orwell'

>>> new_book.publication_year
    # Expected Output: 1949
