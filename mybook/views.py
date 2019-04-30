from django.shortcuts import render, redirect
import requests

from mybook.forms import LoginForm
from mybook.constants import URL_AUTH, URL_BOOK_USER_LIST, COVER_LINK, HEADERS

def mybook_login_requared(view_func):
	def wrapped_view_func(request, *args, **kwargs):
		if request.COOKIES.get('session') is None:
			return redirect('login')
		else:
			return view_func(request, *args, **kwargs)
	return wrapped_view_func


@mybook_login_requared
def books_list(request):
	cookies = {'session': request.COOKIES.get('session')}
	books_list_resp = requests.get(URL_BOOK_USER_LIST,
                     headers=HEADERS, cookies=cookies)
	books = get_books_resp(books_list_resp.json())
	return render(
        request, 'mybook/books.html',
        {'books': books}
    )

def get_books_resp(books_list_resp):
	books = []
	for obj in books_list_resp['objects']:
		book = {k: v for k, v in obj['book'].items() if k in ('name', 'authors_names', 'default_cover')}
		book['cover'] = COVER_LINK + book['default_cover']
		books.append(book)
	return books


def login(request):
	if request.method == 'POST':
		form = LoginForm(request.POST)
		email = request.POST['email']
		password = request.POST['password']
		resp = requests.post(URL_AUTH, 
								data = {
                        			'email': email,
                        			'password': password})
		
		if resp.status_code == 200:
			session_cookie = resp.cookies.get_dict()['session']
			response = redirect('books')
			response.set_cookie(key='session', value=session_cookie)
			return response
		else:
			form = LoginForm()
		return render(
			request, 'login.html',
			{'form': form, 'message' :'Неверно введены данные для входа.' })
	else:
		form = LoginForm()
		return render(
			request, 'login.html',
			{'form': form })



