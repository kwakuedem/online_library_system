from django import forms
from .models import BorrowedBook

class BorrowBookForm(forms.ModelForm):
    class Meta:
        model = BorrowedBook
        fields = ['student', 'book', 'return_date']

    def clean_return_date(self):
        return_date = self.cleaned_data['return_date']
        # Add any custom validation for the return date if needed
        return return_date
