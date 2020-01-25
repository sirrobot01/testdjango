from django.test import TestCase
from django.urls import reverse

from .models import Books


# Create your tests here.


class CreateBookTest(TestCase):

    def setUp(self):
        Books.objects.create(name='Sounds', author='McGraghen', year=2019, pages=45)

    def test_content(self):
        book = Books.objects.get(id=1)
        expected_name = f'{book.name}'
        self.assertEqual(expected_name, 'Sounds')

    def test_template(self):
        response = self.client.get(reverse('add_book'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'create.html')


class ListBookTest(TestCase):
    def setUp(self):
        Books.objects.create(name='Sounds', author='McGraghen', year=2019, pages=45)

    def test_url(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)  # Test response
        self.assertTemplateUsed(response, 'index.html')  # Test templates used
