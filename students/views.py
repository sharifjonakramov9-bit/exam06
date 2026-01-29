# 1 Studentlar ro'yxati
from django.shortcuts import render
from .models import Student
from django.db.models import Q


def student_list(request):
    students = Student.objects.all()

    min_age = request.GET.get('search')
    if min_age:
        students = students.filter(age__gte=min_age)

    search = request.GET.get(search)
    if search:
        students = students.filter(
            Q(full_name__icontains=search) |
            Q(email__icontains=search)
        )

    context = {
        'students': students
        }
    return render(request, 'students/student_list.html', context)