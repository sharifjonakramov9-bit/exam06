# Enrollment Pages
from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.enrollment_create, name='enrollment_create')
]
