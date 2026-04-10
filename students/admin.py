

# Register your models here.
from django.contrib import admin
from .models import Student, Course

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['StdID', 'StdName', 'StdEmail', 'StdAge', 'StdPhone', 'course']
    search_fields = ['StdName', 'StdEmail', 'StdPhone']
    list_filter = ['course']

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['CourseId', 'CourseName', 'CourseZone']
    search_fields = ['CourseName']