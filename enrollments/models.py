# 3️⃣ Enrollment Model (enrollments/models.py)
from django.db import models 
from students.models import Student
from courses.models import Cource

class Enrollments(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='enrollments')
    cource = models.ForeignKey(Cource, on_delete=models.PROTECT, related_name='enrollments')
    enrolled_at = models.DateTimeField(auto_now_add=True)

    class Mata:
        unique_together = ('student', 'course')
        ordering = ['-enrolled_at']

        def __str__(self):
            return f"{self.student} -> {self.course}"
        