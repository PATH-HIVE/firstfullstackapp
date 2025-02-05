
from django import forms
from .models import Student

class StudentForm(forms.ModelForm):
    institution = forms.CharField(max_length=255, required=True)  # Override the default ForeignKey field

    class Meta:
        model = Student
        fields = ['institution', 'programming_language', 'first_name', 'second_name', 'email']
