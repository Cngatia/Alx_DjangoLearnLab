~~~ python

>>> from bookshelf.models import book
>>> book1 = book(tittle="1984", author="George Orwell", publication_year="1949")
>>> book1.save()

>>> from bookshelf.models import book
>>> book.objects.all()
#output: <QuerySet [<book: '1984' by George Orwell>]>
>>> book.objects.values_list('pk', 'title')
#output: <QuerySet [(1,'1984')]>
>>> book1 = book.objects.get(pk=1)
>>> book1
#output: <book: '1984' by George Orwell>

#retrieving all book attributes
>>> book1.title
#output: '1984'
>>> book1.author
#output: 'George Orwell'
>>> book1.publication_year
#output: 1949

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


>>> from bookshelf.models import book
>>> book1 = book.objects.get(pk=1) #saving book to be deleted in variable
>>> book1 #confirming that instance exists
<book: Nineteen Eighty-Four by George Orwell>
>>> book1.delete() #deleting the book
(1, {'bookshelf.book': 1})
>>> book.objects.all() #confirming deletion
<QuerySet []>