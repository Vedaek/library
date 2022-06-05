from django import forms
from library.models import Student
from library.models import Book
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class AddStudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = "__all__"

class AddBookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = "__all__"

class UpdateStudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = "__all__"

class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username","email","password1","password2"]
