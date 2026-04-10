

# Create your views here.
from .models import Student, Course
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

@login_required
def index(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        age = request.POST.get('age', 18)
        phone = request.POST.get('phone', '')
        course_name = request.POST.get('course')

        # Get or create course to handle text input
        course_obj, created = Course.objects.get_or_create(
            CourseName=course_name,
            defaults={'CourseZone': 'General'}
        )
        
        Student.objects.create(
            StdName=name,
            StdEmail=email,
            StdAge=int(age),
            StdPhone=phone if phone else None,
            course=course_obj
        )
        return redirect('/')

    students = Student.objects.all()
    courses = Course.objects.all()
    return render(request, 'index.html', {'students': students, 'courses': courses})

from django.shortcuts import get_object_or_404

def delete_student(request, id):
    student = get_object_or_404(Student, StdID=id)
    student.delete()
    return redirect('/')



from django.shortcuts import render, redirect, get_object_or_404
from .models import Student, Course 

def edit_student(request, id):
    student = get_object_or_404(Student, StdID=id)

    if request.method == 'POST':
        student.StdName = request.POST.get('name')
        student.StdEmail = request.POST.get('email')
        student.StdAge = int(request.POST.get('age', student.StdAge))
        student.StdPhone = request.POST.get('phone', '') or None
        course_name = request.POST.get('course')
        # Get or create course for text input
        student.course, _ = Course.objects.get_or_create(
            CourseName=course_name,
            defaults={'CourseZone': 'General'}
        )
        student.save()
        return redirect('/')

    courses = Course.objects.all()
    return render(request, 'edit.html', {'student': student, 'courses': courses})



