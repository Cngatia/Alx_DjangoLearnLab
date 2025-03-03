from django.urls import path
from .views import BookList,BookViewSet
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token

router = DefaultRouter()
router.register(r'books',BookViewSet,basename='book_all')
urlpatterns = [
  path("books/", BookList.as_view(),name="book_list"),
  path('', include(router.urls)),
  path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
]
