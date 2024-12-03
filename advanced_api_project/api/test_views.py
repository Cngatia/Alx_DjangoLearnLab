from rest_framework.test import APIRequestFactory, APITestCase
from .models import Book, Author
from .serializers import BookSerializer
from rest_framework import status
from django.contrib.auth.models import User  # import User model for login

class BookTests(APITestCase):
    
    def setUp(self):
        # Create an author
        self.author = Author.objects.create(name="J.R.R. Tolkien")
        
        # Create a book
        self.book = Book.objects.create(title="The Lord of the Rings", publication_year=1954, author=self.author)
        
        # Create a user for login
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        
        # Login the user
        self.client.login(username='testuser', password='testpassword')

    def test_get_books(self):
        response = self.client.get('/api/books/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_create_book(self):
        data = {
            'title': 'The Silmarillion',
            'publication_year': 1977,
            'author': self.author.id
        }
        response = self.client.post('/api/books/', data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['title'], data['title'])
        self.assertEqual(response.data['author'], data['author'])
        self.assertEqual(Book.objects.count(), 2)