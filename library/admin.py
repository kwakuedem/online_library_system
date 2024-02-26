# library/admin.py
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import UserProfile, Student, Book, BorrowedBook

class CustomUserAdmin(UserAdmin):
    model = UserProfile
    list_display = ('username','is_active', 'is_staff')
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Permissions', {'fields': ('is_active','is_staff','is_student')}),
    )
admin.site.register(UserProfile, CustomUserAdmin)

class StudentAdmin(admin.ModelAdmin):
    def get_username(self, obj):
        return obj.user.username
    get_username.short_description = 'Username'

    list_display = ('get_username', 'firstname', 'lastname', 'department', 'programme', 'level')
    search_fields = ('user__username', 'firstname', 'lastname', 'level', 'programme')
    list_filter = ('level', 'programme')
admin.site.register(Student, StudentAdmin)

class BorrowedBookAdmin(admin.ModelAdmin):
    def get_student_username(self, obj):
        return obj.student.username
    get_student_username.short_description = 'Student Index No#'

    def get_book_title(self, obj):
        return obj.book.title
    get_book_title.short_description = 'Book Borrowed'

    def get_book_author(self, obj):
        return obj.book.author
    get_book_author.short_description = 'Author of Borrowed Book'
    list_display = ('get_student_username', 'get_book_title', 'get_book_author', 'return_date', 'returned')
    search_fields = ('user__username',)

admin.site.register(BorrowedBook, BorrowedBookAdmin)


class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'available_copies')
    list_filter = ('title','author', 'available_copies')
    search_fields = ('title', 'author',)

admin.site.register(Book,BookAdmin)