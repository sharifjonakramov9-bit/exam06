from django import forms
from .models import Course

class CourseForms(forms.ModelForm):
    
    class Meta:
        model = Course
        fields = ["title", 'description', 'duration_weeks']
