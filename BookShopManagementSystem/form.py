from django import forms
from dashboard.models import Book

class BookForm(forms.modelForm):
    class Meta:
        model = Book
        fields="__all__"