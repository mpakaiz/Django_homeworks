import json

from django.core.management.base import BaseCommand
from books.models import Book


class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        with open('fixtures/books.json', 'r', encoding='utf-8') as file:
            books = json.load(file)
        print(books)
        for book in books:
            new_book = Book()
            new_book.name = book['fields']['name']
            new_book.author = book['fields']['author']
            new_book.pub_date = book['fields']['pub_date']
            new_book.save()

            self.stdout.write(self.style.SUCCESS(f'Successfully added {new_book.name}'))
