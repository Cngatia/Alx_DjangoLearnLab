~~~python 
#create a  new book instance

>>> from bookshelf.models import book
>>> book1 = book(tittle="1984", author="George Orwell", publication_year="1949")
>>> book1.save()
