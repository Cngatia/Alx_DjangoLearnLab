from django.shortcuts import render
from .models import Book
from django.contrib.auth.decorators import permission_required
@permissin_required('bookshelf.can_edit',raise_exception =True)
def book_list(request):
  books = Book.objects.all()
  return render(request,'bookshelf/book_list.html',{'books':books})
@permission_required('bookshelf.can_create',raise_exception =True)
def book_create(request): 
  if request.method == 'POST':
   pass
  return render(request,'bookshelf/book_create.html')
# Create your views here.
from django.views.decorators.csrf import csrf_protect

@csrf_protect
def my_view(request):
    pass
from .forms import ExampleForm

def create_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = BookForm()
    return render(request, 'book_form.html', {'form': form})
from django.views.decorators.csrf import csrf_protect

@csrf_protect
def my_view(request):
    ...