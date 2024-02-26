# library/models.py

from django.contrib.auth.models import AbstractBaseUser,BaseUserManager,PermissionsMixin
from django.db import models



class CustomUserManager(BaseUserManager):
    def create_user(self, username, password=None, **extra_fields):
        if not username:
            raise ValueError('The username field must be set')
        user = self.model(username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(username, password, **extra_fields)

class UserProfile(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=30, unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_student=models.BooleanField(default=True)

    objects = CustomUserManager()

    USERNAME_FIELD = 'username'
        
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.username

class Student(models.Model):
    user = models.OneToOneField(UserProfile, on_delete=models.CASCADE, related_name='student_profile')
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    department = models.CharField(max_length=100)
    programme = models.CharField(max_length=100)
    level = models.CharField(choices=[('100','Level 100'), ('200','Level 200'), ('300','Level 300'), ('400','Level 400')], max_length=255)
    borrowed_books = models.ManyToManyField('Book', related_name='borrowed_by', blank=True)
    
    def __str__(self):
        return f"{self.user.username}"

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    available_copies = models.IntegerField()

    def __str__(self):
        return self.title
    
class BorrowedBook(models.Model):
    student = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    return_date = models.DateField(blank=True, null=True)
    returned=models.BooleanField(default=False)

    def __str__(self):
        return f"{self.student.username} - {self.book}"