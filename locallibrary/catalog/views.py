from django.shortcuts import render

# Create your views here.
from .models import Book, Author, BookInstance, Genre

from django.views import generic


def index(request):
    """View function for home page of site."""
    # Generate counts of some of the main objects
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()
    # Available copies of books (status = 'a')
    num_instances_available = BookInstance.objects.filter(
        status__exact='a').count()
    num_authors = Author.objects.count()  # The 'all()' is implied by default.

    # Number of visits to this view, as counted in the session variable.
    num_visits = request.session.get('num_visits', 1)
    request.session['num_visits'] = num_visits + 1

    # Render the HTML template index.html with the data in the context variable.
    return render(
        request,
        'index.html',
        context={
            'num_books': num_books,
            'num_instances': num_instances,
            'num_instances_available': num_instances_available,
            'num_authors': num_authors,
            'num_visits': num_visits
        },
    )


class BookListView(generic.ListView):
    # The generic view will query the database to get all records for the specified model (Book)
    model = Book

    # your own name for the list as a template variable, default 'objects_list' or 'the_model_name_list'
    context_object_name = 'book_list'

    # Get 5 books containing the title war, default model-name.objects.all()
    queryset = Book.objects.filter(title__icontains='war')[:5]

    # Specify your own template name/location, if the specify tempplate file isn't existed,
    # that will use default templates_directory/application_directory/the_model_name_list.html
    template_name = 'catalog/template_name_list.html'
