from django.shortcuts import render_to_response

from books.models import Book


def search(request):
    error = False
    if 'name' in request.GET or 'author' in request.GET:
        name = request.GET['name']
        author = request.GET['author']
        if not name and not author:
            error = True
        elif name and author:
            books = Book.objects.filter(author__icontains=author, name__icontains=name)
            return render_to_response('search_results.html',
                                      {'books': books, 'query': author + '-' + name})
        elif name:
            books = Book.objects.filter(name__icontains=name)
            return render_to_response('search_results.html', {'books': books, 'query': name})
        elif author:
            books = Book.objects.filter(author__icontains=author)
            return render_to_response('search_results.html', {'books': books, 'query': author})
    return render_to_response('search_form.html', {'error': error})
