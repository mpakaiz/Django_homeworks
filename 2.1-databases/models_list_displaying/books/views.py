import json
from django.core.paginator import Paginator
from django.shortcuts import render
from django.views import View
from books.models import Book


def books_view(request):
    template = 'books/books_list.html'
    books = Book.objects.all()
    context = {
        "books": books
    }
    return render(request, template, context)



def book_view(request):
    template = 'books/book.html'
    books_list = []
    pub_dates = []
    with open('fixtures/books.json', 'r', encoding='utf-8') as file:
        books = json.load(file)

        for book in books:
            new_book = {
                'name': book['fields']['name'],
                'author': book['fields']['author'],
                'pub_date': book['fields']['pub_date'],
            }
            books_list.append(new_book)
            pub_date = {
                'pub_date': new_book['pub_date']
            }
            pub_dates.append(pub_date)

    page_number = int(request.GET.get('page', 1))
    paginator = Paginator(books_list, 1)
    page = paginator.get_page(page_number)
    num_pages = paginator.num_pages
    if page_number != 0 and page_number != num_pages:
        pub_dates_prev = pub_dates[page_number - 1]
        pub_dates_next = pub_dates[page_number]
    elif page_number == num_pages:
        pub_dates_prev = pub_dates[page_number - 1]
        pub_dates_next = ''
    else:
        pub_dates_prev = ''
        pub_dates_next = pub_dates[page_number]

    context = {
        'books': books_list,
        'pub_dates_prev': pub_dates_prev,
        'pub_dates_next': pub_dates_next,
        'page': page
    }
    return render(request, template, context)


