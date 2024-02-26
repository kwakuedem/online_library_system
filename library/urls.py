# library/urls.py
from django.urls import path
from .views import index,user_dashboard,my_logout_view, borrow_book, check_borrowed_books,CustomLoginView

urlpatterns = [
    path('', index, name='index'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('dashboard/', user_dashboard, name='user_dashboard'),
    path('logout/', my_logout_view, name='logout'),  # Add this line
    path('borrow_book/', borrow_book, name='borrow_book'),
    # path('borrow/<int:student_id>/', borrow_book, name='borrow_book'),
    path('check_borrowed_books/', check_borrowed_books, name='borrowed_books'),
    path('check_borrowed_books/<int:student_id>/', check_borrowed_books, name='check_borrowed_books'),
]