
# Create your models here.

# from django.db import models

# class Student(models.Model):
#     name = models.CharField(max_length=100)
#     email = models.EmailField()
#     course = models.CharField(max_length=100)

#     def __str__(self):
#         return self.name

from django.db import models

class Course(models.Model):
    CourseId = models.AutoField(primary_key=True)
    CourseName = models.CharField(max_length=100)
    CourseZone = models.CharField(max_length=100)

    class Meta:
        db_table = 'course'   # EXACT table name in MySQL

    def __str__(self):
        return self.CourseName


class Student(models.Model):
    StdID = models.AutoField(primary_key=True)
    StdName = models.CharField(max_length=100)
    StdAge = models.IntegerField()
    StdEmail = models.EmailField()
    StdPhone = models.CharField(max_length=15, blank=True, null=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    class Meta:
        db_table = 'student'   # EXACT table name in MySQL

    def __str__(self):
        return self.StdName