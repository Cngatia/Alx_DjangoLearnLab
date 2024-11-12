~~~python

>>> from bookshelf.models import book
>>> book1 = book.objects.get(pk=1)#retrieveing book to be updated
>>> book1 #confirming the right book was retrieved
<book: 1984 by George Orwell>
>>> book1.title = 'Nineteen Eighty-Four'
>>> book1
<book: Nineteen Eighty-Four by George Orwell>
>>> book1.save() #saving the new changes to db
>>> book1 #confirming update was successful
#output: <book: 'Nineteen Eighty-Four' by George Orwell