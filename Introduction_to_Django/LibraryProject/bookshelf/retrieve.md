~~~ python

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