# 2️⃣ Student Model (students/models.py)
from django.db import models
from django.core.exceptions import ValidationError


class Student(models.Model):
    full_name = models.CharField(max_length=150)
    email = models.EmailField(unique=True)
    age = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def clean(self):
        if self.age < 16:
            raise ValidationError({
                'age': 'Student has to be at least 16 years old'
            })
        
        def __str__(self):
            return self.full_name
        