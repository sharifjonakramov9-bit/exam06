# 1️⃣ Course Model (courses/models.py)
from django.db import models
from django.core.exceptions import ValidationError

class Cource(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    duration_weeks = models.PositiveBigIntegerField()
    created_at = models.DateField(outo_now_add=True)

    def clean(self):
        if self.duration_weeks <= 0:
            raise ValidationError({
                'duration_weeks': 'Duration must be bigger then 0'
            })
        
    def __str__(self):
        return self.title
