
![image alt](https://github.com/MrFaizahmed/student-management-system/blob/a995b8d3c299dc90cb49e21d97adaa6a8f7e57f1/Screenshot%202026-04-08%20193928.png)


![image alt](https://github.com/devallasimhadri/Student-Management-System/blob/495ea43bf5c3e9371c58a3991fdeabab4341f3ea/Screenshot%202026-04-10%20102516.png)

![image alt](https://github.com/MrFaizahmed/student-management-system/blob/c00338c384b9e2549974d73e9c5f8a6eeb2dcfc7/Screenshot%202026-04-08%20194123.png)

![image alt](https://github.com/MrFaizahmed/student-management-system/blob/4b5404af1e55d7e8ca5a762aa65e5a67f326c52d/Screenshot%202026-04-08%20194140.png)












# Student Management System

A complete student management system built with Python, Django, and MySQL database.

## Features

- ✅ Add new students
- ✅ View all students
- ✅ Edit student information
- ✅ Delete students
- ✅ Course management
- ✅ User authentication (login/logout)
- ✅ MySQL database integration
- ✅ Responsive Bootstrap UI

## Technology Stack

- **Backend**: Python 3.x, Django 4.0+
- **Database**: MySQL 8.0+
- **Frontend**: HTML5, Bootstrap 5
- **Authentication**: Django Authentication System

## Project Structure

```
student_mng/
├── student_project/          # Django project settings
│   ├── settings.py           # Configuration (database, apps, etc.)
│   ├── urls.py               # URL routing
│   └── wsgi.py               # WSGI application
├── students/                 # Main application
│   ├── models.py             # Database models (Student, Course)
│   ├── views.py              # Business logic
│   ├── urls.py               # App URLs
│   ├── templates/            # HTML templates
│   │   ├── index.html        # Main page
│   │   ├── edit.html         # Edit student page
│   │   └── registration/
│   │       └── login.html    # Login page
│   └── migrations/           # Database migrations
├── manage.py                 # Django management script
├── requirements.txt          # Python dependencies
└── MYSQL_SETUP_GUIDE.md      # Detailed MySQL setup guide
```

## Installation & Setup

### Step 1: Prerequisites

Make sure you have:
- Python 3.8 or higher installed
- MySQL Server 8.0+ installed and running
- pip (Python package manager)

### Step 2: Install Dependencies

```bash
cd student_mng
pip install -r requirements.txt
```

### Step 3: Setup MySQL Database

Run the interactive setup script:

```bash
python setup_database.py
```

This will:
- Prompt for your MySQL credentials
- Create the `student_management` database
- Provide next steps

**Alternative**: See `MYSQL_SETUP_GUIDE.md` for manual setup instructions.

### Step 4: Configure Database Connection

The database settings are already configured in `student_project/settings.py`:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'student_management',
        'USER': 'root',
        'PASSWORD': '',  # Update with your password
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
```

**Important**: Update the `PASSWORD` field with your actual MySQL password.

### Step 5: Run Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### Step 6: Create Admin Superuser

```bash
python manage.py createsuperuser
```

Enter your desired username, email, and password.

### Step 7: (Optional) Add Sample Courses

To add some initial courses, run:

```bash
python manage.py shell
```

Then execute:

```python
from students.models import Course
Course.objects.create(CourseName='Computer Science', CourseZone='IT')
Course.objects.create(CourseName='Business Administration', CourseZone='Management')
Course.objects.create(CourseName='Engineering', CourseZone='Technical')
exit()
```

### Step 8: Run Development Server

```bash
python manage.py runserver
```

Visit http://127.0.0.1:8000/ in your browser.

## Usage

### Accessing the System

1. **Login**: Navigate to http://127.0.0.1:8000/accounts/login/
2. Enter your superuser credentials
3. You'll be redirected to the main dashboard

### Managing Students

#### Add a Student
1. Fill in the form at the top of the page:
   - Student Name
   - Email Address
   - Age
   - Select Course from dropdown
2. Click "Add Student"

#### View Students
- All students are displayed in a table below the form
- Shows: Name, Email, Course

#### Edit a Student
1. Click the "Edit" button next to any student
2. Modify the information
3. Click "Update Student"

#### Delete a Student
- Click the "Delete" button next to any student
- The student will be immediately removed

### Admin Panel

Access the Django admin panel at: http://127.0.0.1:8000/admin/

Here you can:
- Manage students
- Manage courses
- Manage users
- View database records

## Database Models

### Course Model
```python
class Course(models.Model):
    CourseId = models.AutoField(primary_key=True)
    CourseName = models.CharField(max_length=100)
    CourseZone = models.CharField(max_length=100)
```

### Student Model
```python
class Student(models.Model):
    StdID = models.AutoField(primary_key=True)
    StdName = models.CharField(max_length=100)
    StdAge = models.IntegerField()
    StdEmail = models.EmailField()
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
```

## API Endpoints

- `GET /` - View all students
- `POST /` - Add new student
- `GET /edit/<id>/` - Edit student form
- `POST /edit/<id>/` - Update student
- `GET /delete/<id>/` - Delete student
- `GET /accounts/login/` - Login page
- `POST /accounts/logout/` - Logout

## Troubleshooting

### Database Connection Error

If you see "Access denied for user":
1. Verify MySQL is running
2. Check username/password in `settings.py`
3. Ensure database exists

### Migration Errors

If migrations fail:
```bash
# Delete migration files (except __init__.py)
# Then run:
python manage.py makemigrations
python manage.py migrate
```

### Module Not Found: MySQLdb

Ensure pymysql is installed and configured:
```bash
pip install pymysql
```

Check that these lines exist in `settings.py`:
```python
import pymysql
pymysql.install_as_MySQLdb()
```

## Security Notes

⚠️ **For Development Only**: This configuration is for local development only.

For production deployment:
1. Set `DEBUG = False` in settings.py
2. Use environment variables for sensitive data (passwords, secret key)
3. Configure proper `ALLOWED_HOSTS`
4. Use HTTPS
5. Set up proper database user with limited privileges
6. Never commit passwords to version control

## License

This project is open source and available for educational purposes.

## Support

For issues or questions:
1. Check `MYSQL_SETUP_GUIDE.md` for detailed database setup
2. Review Django documentation: https://docs.djangoproject.com/
3. Check MySQL documentation: https://dev.mysql.com/doc/


