"""
Script to add sample courses to the database
Run this after migrations with: python manage.py shell < add_sample_courses.py
"""

from students.models import Course

print("Adding sample courses...")

# Sample courses
courses_data = [
    {'name': 'Computer Science', 'zone': 'IT'},
    {'name': 'Business Administration', 'zone': 'Management'},
    {'name': 'Engineering', 'zone': 'Technical'},
    {'name': 'Mathematics', 'zone': 'Science'},
    {'name': 'English Literature', 'zone': 'Arts'},
]

created_count = 0
for course_data in courses_data:
    course, created = Course.objects.get_or_create(
        CourseName=course_data['name'],
        defaults={'CourseZone': course_data['zone']}
    )
    if created:
        print(f"✓ Created: {course.CourseName}")
        created_count += 1
    else:
        print(f"- Already exists: {course.CourseName}")

print(f"\n{created_count} new courses created!")
print(f"Total courses: {Course.objects.count()}")
