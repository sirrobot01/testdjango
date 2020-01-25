from django.urls import path, include
from .views import CreateBook, ListBook

urlpatterns = [
    path('', ListBook.as_view(), name='home'),
    path('add/', CreateBook.as_view(), name='add_book')
]