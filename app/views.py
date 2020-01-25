from django.shortcuts import render
from django.urls import reverse_lazy

from .models import Books
from django.views import generic
from .forms import BookForm
# Create your views here.



class CreateBook(generic.CreateView):
    model = Books
    template_name = 'create.html'
    form_class = BookForm
    success_url = reverse_lazy('home')

class ListBook(generic.ListView):
    queryset = Books.objects.all()
    template_name = 'index.html'
    context_object_name = 'books'

