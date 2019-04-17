from django.shortcuts import render

def books_list(request):
	books = []
	return render(
        request, 'mybook/books.html',
        {'books': books}
    )
