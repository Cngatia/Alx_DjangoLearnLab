from .models import Book, Library, Librarian,Author
author_name = "John Doe"
author = Author.objects.get(name=author_name) 
Book.objects.filter(author=author)

library_name = "My Library"
library = Library.objects.get(name=library_name)
books = library.books.all()  
for book in books:
    print(book)


librarians = Librarian.objects.get(library="library_name")  


for librarian in librarians:
    print(librarian)