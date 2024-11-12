~~~ python

>>> from bookshelf.models import book
>>> book1 = book.objects.get(pk=1) #saving book to be deleted in variable
>>> book1 #confirming that instance exists
<book: Nineteen Eighty-Four by George Orwell>
>>> book1.delete() #deleting the book
(1, {'bookshelf.book': 1})
>>> book.objects.all() #confirming deletion
<QuerySet []>