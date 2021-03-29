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
    """View Class for the book list page"""
    # The generic view will query the database to get all records for the specified model (Book)
    model = Book

    # your own name for the list as a template variable, default 'objects_list' or 'the_model_name_list'
    context_object_name = 'book_list'

    # Get 5 books containing the title war, default model-name.objects.all()
    # queryset = Book.objects.filter(title__icontains='war')[:5]

    # Specify your own template name/location, if the specify tempplate file isn't existed,
    # that will use default templates_directory/application_directory/the_model_name_list.html
    # template_name = 'TEMPLATE_NAME'

    # The page_obj is a Paginator object that will exist if pagination is being used on the current page.
    # Add pagination to your list views, reducing the number of items displayed on each page.
    # The different pages are accessed using GET parameters, e.g. /catalog/books/?page=2.
    paginate_by = 10

    def get_queryset(self):
        """
        Change the list of records returned. This is more flexible than just setting the queryset attribute.
        """
        queryset = super(BookListView, self).get_queryset()
        queryset = queryset  # TODO
        # e.g. Get 5 books containing the title war
        # queryset = Book.objects.filter(title__icontains='war')[:5]
        return queryset

    def get_context_data(self, **kwargs):
        """
        Pass additional context variables to the template (e.g. the list of books is passed by default). 
        When doing this it is important to follow the pattern used below.
        """
        # Call the base implementation first to get the context
        context = super(BookListView, self).get_context_data(**kwargs)
        # Create any data and add it to the context
        # Number of visits to this view, as counted in the session variable.
        book_list_num_visits = self.request.session.get('book_list_num_visits', 1)
        self.request.session['book_list_num_visits'] = book_list_num_visits + 1
        context['book_list_num_visits'] = book_list_num_visits
        # return the new (updated) context.
        return context


class BookDetailView(generic.DetailView):
    """View class for book detail page"""
    model = Book


class AuthorListView(generic.ListView):
    """View class for author list page"""
    model = Author
    paginate_by = 10


class AuthorDetailView(generic.DetailView):
    """View class for author detail page"""
    model = Author
