from django.urls import path
from .views import list_books, LibraryDetailView
urlpatterns = [
  path('', list_books, name='index'),
  path('detail', LibraryDetailView.as_view(), name='detail'),
]






from django.contrib.auth.views import LoginView,LogoutView
from django.urls import path
from . import views

# urlpatterns = [
#     path('login/', LoginView.as_view(template_name='registration/login.html'), name='login'),
#     path('logout/', LogoutView.as_view(template_name="logout.html"), name='logout'),
#     path('register/', views.register, name='register'),
# ]











urlpatterns = [
    path('admin/', views.admin_view, name='admin_view'),
    path('librarian/', views.librarian_view, name='librarian_view'),
    path('member/', views.member_view, name='member_view'),
]






# urlpatterns = [
#     path('add_book/', views.add_book, name='add_book'),
#     path('edit_book/', views.edit_book, name='edit_book'),
#     path('delete_book/', views.delete_book, name='delete_book'),
# ]