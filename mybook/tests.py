from django.test import TestCase
from django.urls import reverse
import json

from mybook.views import books_list, get_books_resp, login
from mybook import test_data

class GetBooksFromRespTest(TestCase):

	def test_empty_resp(self):
		json_empty_resp = json.loads(test_data.EMPTY_RESP)
		self. assertEquals(get_books_resp(json_empty_resp), [])

	def test_one_book_resp(self):
		json_one_book_resp = json.loads(test_data.ONE_BOOK_RESP)
		self.assertEquals(get_books_resp(json_one_book_resp), test_data.ONE_BOOK_DATA)

	def test_books_resp(self):
		json_books_resp = json.loads(test_data.BOOKS_RESP)
		self.assertEquals(get_books_resp(json_books_resp), test_data.BOOKS_DATA)


