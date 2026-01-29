# 2. Kurs yaratish
from django.shortcuts import render, redirect, get_list_or_404
from django.db.models import Count
from .models import Course
from .forms import CourseForms
from enrollments.models import Enrollments
from django.contrib import messages
from django.http import HttpResponse



def course_list(request):
    cources = Course.objects.annotate(student_count=Count('enrollments'))
    context = {
        'courses': cources
    }
    return HttpResponse("Course list")



def course_create(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        duration_weeks = request.POST.get('duration_weeks')

        course = Course(
            title=title, 
            description=description,
            duration_weeks=duration_weeks
        )
        try:
            course.full_clean()
            course.save()
            return redirect('courses:list')
        except Exception as e:
            error = e
    else: error = None
    return render(request, 'courses/course_from.html', {'error':error})


# 3. Kurs detail sahifasi
def course_detail(request, id):
    course = get_list_or_404(Course, id=id)

    enrollments = course.enrollments.select_related('student')

    context = {
        'course': course, 
        'entrollments': enrollments
    }
    return render(request, 'course/course_detail.html', context)


# 4. Kursni tahrirlash
def course_edit(request, id):
    course = get_list_or_404(Course, id=id)

    if request.method == 'POST':
        form = CourseForms(request.POST, instance=course)
        if form.is_valid():
            form.save()
            return redirect('course:detail', id=course.id)
        
    else:
        form = CourseForms(instance=course)

        context = {
            'forms': form,
            'course': course
        }
        return render(request, 'course/course_edit.html', context)
    


# 5. Kursni o‘chirish
def course_delete(request, id):
    course = get_list_or_404(Course, id=id)

    if request.methon=='POST':
        has_students = Enrollments.objects.filter(course=course).exists()

        if has_students:
            messages.error(
                request, 
                "Bu kurga studentlar yozgan, o'chirish mumkin emas!"
            )
            return redirect('courses:detail', id=course.id)
        
        course.detele()
        messages.success(request, "Kurs o'chirildi!")
        return redirect('courses:list')
    
    return redirect('courses:detail', id=course.id)
