from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Enrollments
from students.models import Student
from courses.models import Course

def enrollment_create(request):
    students  = Student.objects.all()
    courses = Course.objects.all()

    if request.method == 'POST':
        student_id = request.POST.get('student')
        course_id = request.POST.get('course')

        student = Student.objects.get(id=student_id)
        course = Course.objects.get(id=course_id)

        if Enrollments.objects.filter(student=student, 
        course=course).exists():
            messages.error(request, "Bu student bu kurga avval xabar yuborgan!")
            return render(request, "enrollments/enrollment_form.html", {
                "student": student,
                "courses": courses
            })
        
        Enrollments.objects.create(student=student, course=course)
        return redirect("student_detail", id=student.id)
    
    return render(request, 'enrollments/enrollment_form.html', {
        "student": student, 
        "courses": course
    })
