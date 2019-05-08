from django.test import TestCase
from django.urls import reverse
from django.http import HttpRequest
from mock import Mock
import json

from mybook import views, test_data

class GetBooksFromRespTest(TestCase):

	def test_empty_resp(self):
		json_empty_resp = json.loads(test_data.EMPTY_RESP)
		self.assertEquals(views.get_books_resp(json_empty_resp), [])

	def test_one_book_resp(self):
		json_one_book_resp = json.loads(test_data.ONE_BOOK_RESP)
		self.assertEquals(views.get_books_resp(json_one_book_resp), test_data.ONE_BOOK_DATA)

	def test_books_resp(self):
		json_books_resp = json.loads(test_data.BOOKS_RESP)
		self.assertEquals(views.get_books_resp(json_books_resp), test_data.BOOKS_DATA)


class TestMyBookLoginRequired(TestCase):

	def test_not_auth(self):
		func =  Mock()
		decorated_func = views.mybook_login_requared(func)
		request = HttpRequest()
		resp = decorated_func(request)
		self.assertIs(func.called, False)

	def test_auth(self):
		func =  Mock()
		decorated_func = views.mybook_login_requared(func)
		request = HttpRequest()
		request.COOKIES['session'] = test_data.SESSION_COOKIE
		resp = decorated_func(request)
		self.assertIs(func.called, True)