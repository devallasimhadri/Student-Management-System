# MySQL Database Setup for Student Management System

## Prerequisites
- MySQL Server 8.0+ installed and running
- Python 3.x installed
- Django 4.0+ installed

## Step 1: Create MySQL Database

### Option A: Using MySQL Command Line
```bash
mysql -u root -p
```
Then enter your MySQL root password and run:
```sql
CREATE DATABASE student_management;
```

### Option B: Using MySQL Workbench
1. Open MySQL Workbench
2. Connect to your MySQL server
3. Run this SQL command:
```sql
CREATE DATABASE student_management;
```

## Step 2: Update Database Configuration

Open `student_project/settings.py` and update the DATABASES section with your MySQL credentials:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'student_management',
        'USER': 'root',              # Your MySQL username
        'PASSWORD': 'your_password',  # Your MySQL password (CHANGE THIS!)
        'HOST': 'localhost',
        'PORT': '3306',
        'OPTIONS': {
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'"
        }
    }
}
```

## Step 3: Install Required Packages

```bash
pip install pymysql mysqlclient
```

## Step 4: Run Migrations

Navigate to the project directory and run:

```bash
python manage.py makemigrations
python manage.py migrate
```

## Step 5: Create Superuser (Admin)

```bash
python manage.py createsuperuser
```

Follow the prompts to set up your admin account.

## Step 6: Add Sample Data (Optional)

You can add sample courses through Django admin or shell:

```bash
python manage.py shell
```

```python
from students.models import Course
Course.objects.create(CourseName='Computer Science', CourseZone='IT')
Course.objects.create(CourseName='Business Administration', CourseZone='Management')
Course.objects.create(CourseName='Engineering', CourseZone='Technical')
```

## Step 7: Run Development Server

```bash
python manage.py runserver
```

Visit http://127.0.0.1:8000/ in your browser.

## Troubleshooting

### Error: "Access denied for user 'root'@'localhost'"
- Make sure you're using the correct MySQL password
- Check if MySQL user has proper permissions

### Error: "No module named 'MySQLdb'"
- Make sure pymysql is installed: `pip install pymysql`
- Verify that `import pymysql` and `pymysql.install_as_MySQLdb()` are in settings.py

### Error: Database connection failed
- Ensure MySQL server is running
- Check HOST and PORT settings
- Verify firewall settings allow connections on port 3306
