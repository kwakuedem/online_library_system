# library/views.py
from django.contrib.auth import logout as auth_logout
from django.http import HttpResponseForbidden, HttpResponseServerError
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.contrib import messages
from django.urls import reverse_lazy
from library.form import BorrowBookForm
from .models import Student, Book, UserProfile, BorrowedBook


#function to render the index page
def index(request):
    return render(request, 'index.html')

class CustomLoginView(LoginView):
    template_name = 'login.html'

    def get_success_url(self):
        # Redirect to the appropriate dashboard based on user role
        if self.request.user.is_active:
            return reverse_lazy('user_dashboard')
        else:
            return reverse_lazy('index')


@login_required
def user_dashboard(request):
    return render(request, 'dashboard.html')


@login_required
def borrow_book(request):
    print("Borrow book")
    user = request.user
    if not user.is_student:
        messages.error(request, 'You do not have permission to access this page.')
        return redirect('index')
    student = get_object_or_404(Student, pk=user.id)

    if request.method == 'GET':
        books = Book.objects.all()
        print(books)
        return render(request, 'borrow_book.html', {'student': student, 'books': books})

    if request.method == 'POST':
        # ... handle book borrowing
        messages.success(request, 'Book borrowed successfully.')
        return redirect('index')
    
    
@login_required
def check_borrowed_books(request, student_id):
    if not request.user.is_librarian:
        messages.error(request, 'You do not have permission to access this page.')
        return redirect('index')
    student = get_object_or_404(Student, pk=student_id)
    borrowed_books = student.borrowed_books.all()
    return render(request, 'check_borrowed_books.html', {'student': student, 'borrowed_books': borrowed_books})

# logout view to handle logout request
@login_required
def my_logout_view(request):
    auth_logout(request)
    return redirect('index')

@login_required
def borrow_book(request):
    if request.method == 'POST':
        if request.user.is_authenticated:
            student = get_object_or_404(UserProfile, pk=request.user.id)
            form = BorrowBookForm(request.POST)
            if form.is_valid():
                # Associate the student with the borrowed book
                book = form.save(commit=False)
                book.student = student
                book.save()
                return redirect('user_dashboard')
            else:
                print("Error",  form.errors)
                # Handle the case where the form is not valid (e.g., show an error message)
                return render(request, 'borrow_book.html', {'form': form, 'books': Book.objects.all(), "errors":form.errors})
        else:
            # Handle the case where the user is not authenticated
            return HttpResponseForbidden("You need to be logged in to borrow a book.")

    if request.method == 'GET':
        form = BorrowBookForm()
        books = Book.objects.all()
        return render(request, 'borrow_book.html', {'form': form, 'books': books})
    # This is a fallback to prevent the view from returning None
    return HttpResponseServerError("An unexpected error occurred.")

@login_required
def check_borrowed_books(request):
    student = request.user
    books = BorrowedBook.objects.filter(student=student.id)
    return render(request, 'check_borrowed_books.html', {"borrowed_books":books})
