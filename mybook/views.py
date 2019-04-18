from django.shortcuts import render
import requests

EMAIL = 'some_mail@mail.ru'
PASSWARD = 'password'
URL_AUTH = "https://mybook.ru/api/auth/"
URL_BOOK_USER_LIST = "https://mybook.ru/api/bookuserlist/"
HEADERS = {'Accept': 'application/json; version=5'}

def books_list(request):
	session = requests.Session()
	resp = session.post(URL_AUTH, 
						data = {
                        	'email': EMAIL,
                        	'password': PASSWARD})
	books_list_resp = session.get(URL_BOOK_USER_LIST,
                     headers=HEADERS)
	books = get_books_resp(books_list_resp)
	return render(
        request, 'mybook/books.html',
        {'books': books}
    )

def get_books_resp(books_list_resp):
	books = []
	for obj in books_list_resp.json()['objects']:
		book = {k: v for k, v in obj['book'].items() if k in ('name', 'authors_names', 'default_cover')}
		books.append(book)
	return books