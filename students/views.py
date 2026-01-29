# 1 Studentlar ro'yxati
from django.shortcuts import render, redirect, get_list_or_404
from .models import Student
from django.db.models import Q
from django.core.exceptions import ValidationError
from enrollments.models import Enrollments


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


# 2 Student yaratish
def student_create(request):
    if request.method == 'POST':
        full_name = request.POST.get('full_name')
        email = request.POST.get('email')
        age = request.POST.get('age')

        student = Student(
            full_name=full_name, 
            email=email, 
            age=age
        )
        try:
            student.save()
            return redirect('student_list')
        except ValidationError as e:
            error = e.message_dict

        else:
            error = None
            
        return render(request, 'students/student_create.html', {
            'error': error
        })
    


# 3 Student detail
def student_detail(request, id):
    student = get_list_or_404(Student, id=id)

    enrollments = Enrollments.objects.filter(student=student)

    return render(request, 'students/student_detail.html', {
        'student': student,
        'enrollments': enrollments
    })

# 4 Student delete
def student_delete(request, id):
    student = get_list_or_404(Student, id=id)

    has_enrollments = Enrollments.objects.filter(student=student).exists()
    if has_enrollments:
        return render(request, 'students/student_delete_error,html', {
            'student': student
        })
    if request.method == 'POST':
        Student.delete()
        return redirect