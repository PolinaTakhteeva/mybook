from django.contrib import admin
from django.urls import path, include
from mybook import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('books/', views.books_list, name='books'),
    path('login/', views.login, name='login')
]
