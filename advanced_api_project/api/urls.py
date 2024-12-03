from django.urls import path,include
from . import views
# from rest_framework.routers import DefaultRouter
# from .views import Bookviewset,Authorviewset
# router = DefaultRouter()
# router.register(r"books",Bookviewset)
# router.register(r"authors",Authorviewset)
# urlpatterns = [
#   path("",include(router.urls)),
# ]

urlpatterns = [
  path("books/",views.BookListView.as_view(),name ='list-book'),
  path("books/<int:pk>/",views.BookDetailView.as_view(),name='detail-book'),
  path("books/create/",views.BookCreateView.as_view(),name ='create-book'),
  path("books/delete/<int:pk>/)",views.BookDeleteView.as_view(),name='delete-book'),
  path("books/update/<int:pk>/)",views.BookUpdateView.as_view(),name='update-book')]