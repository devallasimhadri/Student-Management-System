# Visual Setup Guide - Student Management System

## 🎯 Complete Setup Process in 7 Steps

```
┌─────────────────────────────────────────────────────────────────┐
│                    STEP 1: INSTALL DEPENDENCIES                 │
└─────────────────────────────────────────────────────────────────┘
                              ↓
    Open terminal in project directory and run:
    
    $ pip install -r requirements.txt
    
                              ↓
    ✓ Django installed
    ✓ PyMySQL installed
    ✓ mysqlclient installed
                              ↓
┌─────────────────────────────────────────────────────────────────┐
│                  STEP 2: CREATE MYSQL DATABASE                  │
└─────────────────────────────────────────────────────────────────┘
                              ↓
    Run the interactive setup script:
    
    $ python setup_database.py
    
                              ↓
    Enter your MySQL credentials:
    • Username: root (or your username)
    • Password: ******** (your MySQL password)
    • Host: localhost (default)
    • Port: 3306 (default)
                              ↓
    ✓ Database 'student_management' created
                              ↓
┌─────────────────────────────────────────────────────────────────┐
│                STEP 3: UPDATE DATABASE PASSWORD                 │
└─────────────────────────────────────────────────────────────────┘
                              ↓
    Open: student_project/settings.py
    Find line ~82:
    
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'student_management',
            'USER': 'root',
            'PASSWORD': '',  ← PUT YOUR PASSWORD HERE
            'HOST': 'localhost',
            'PORT': '3306',
        }
    }
    
                              ↓
    Save the file
                              ↓
┌─────────────────────────────────────────────────────────────────┐
│                   STEP 4: RUN DATABASE MIGRATIONS               │
└─────────────────────────────────────────────────────────────────┘
                              ↓
    Run these commands in order:
    
    $ python manage.py makemigrations
    $ python manage.py migrate
    
                              ↓
    Creating migrations... ✓
    Applying migrations...
     • auth
     • contenttypes
     • sessions
     • students ✓
                              ↓
┌─────────────────────────────────────────────────────────────────┐
│                    STEP 5: CREATE ADMIN USER                    │
└─────────────────────────────────────────────────────────────────┘
                              ↓
    Run:
    
    $ python manage.py createsuperuser
    
                              ↓
    Enter details:
    Username: admin
    Email: admin@example.com (optional)
    Password: ********
    Password (again): ********
    
                              ↓
    Superuser created successfully! ✓
                              ↓
┌─────────────────────────────────────────────────────────────────┐
│              STEP 6: ADD SAMPLE COURSES (OPTIONAL)              │
└─────────────────────────────────────────────────────────────────┘
                              ↓
    Run:
    
    $ python manage.py shell < add_sample_courses.py
    
                              ↓
    Adding sample courses...
    ✓ Created: Computer Science
    ✓ Created: Business Administration
    ✓ Created: Engineering
    ✓ Created: Mathematics
    ✓ Created: English Literature
    
    5 new courses created! ✓
                              ↓
    Or skip this step and add courses later via admin panel
                              ↓
┌─────────────────────────────────────────────────────────────────┐
│                  STEP 7: START DEVELOPMENT SERVER               │
└─────────────────────────────────────────────────────────────────┘
                              ↓
    Run:
    
    $ python manage.py runserver
    
                              ↓
    Watching for file changes...
    Starting development server at http://127.0.0.1:8000/
    
    Quit the server with CTRL-BREAK.
                              ↓
    Server running! ✓
                              ↓
```

---

## 🌐 Access Your Application

### Main Application
```
URL: http://127.0.0.1:8000/

You'll see:
┌──────────────────────────────────────┐
│   Student Management System          │
│                                      │
│   Welcome, admin 👋 [Logout]        │
│                                      │
│   ─────────────────────────────      │
│                                      │
│   Add Student                        │
│   ┌──────┬──────┬────┬──────┬─────┐ │
│   │ Name │Email │Age │Course│ [Add]│ │
│   └──────┴──────┴────┴──────┴─────┘ │
│                                      │
│   Student List                       │
│   ┌─────────────────────────────┐   │
│   │ Name │ Email │ Course │ ... │   │
│   ├─────────────────────────────┤   │
│   │ John │ j@e.c │ CS     │Edit │   │
│   └─────────────────────────────┘   │
└──────────────────────────────────────┘
```

### Login Page
```
URL: http://127.0.0.1:8000/accounts/login/

┌────────────────────────────┐
│  Student Management System │
│         Login              │
│                            │
│  Username: [__________]    │
│  Password: [__________]    │
│                            │
│  [        Login        ]   │
└────────────────────────────┘
```

### Admin Panel
```
URL: http://127.0.0.1:8000/admin/

┌─────────────────────────────────┐
│  Django Administration          │
│                                 │
│  Site Administration            │
│                                 │
│  Students                       │
│  › Students                     │
│  › Courses                      │
│                                 │
│  Authentication and Authorization│
│  › Groups                       │
│  › Users                        │
└─────────────────────────────────┘
```

---

## 📊 Data Flow Diagram

```
User Action → Browser Request → Django Server
                                      ↓
                              URL Routing (urls.py)
                                      ↓
                              View Function (views.py)
                                      ↓
                              Authentication Check
                                      ↓
                              Model Query (models.py)
                                      ↓
                              MySQL Database Query
                                      ↓
                              Results Returned
                                      ↓
                              Template Rendered (HTML)
                                      ↓
                              Response to Browser
                                      ↓
User Sees Updated Page
```

---

## 🗄️ Database Schema Visualization

```
MySQL Server: localhost:3306
Database: student_management
│
├─ Tables Created by Django Migrations:
│  ├─ auth_user (Django authentication)
│  ├─ auth_group
│  ├─ django_session
│  ├─ django_content_type
│  │
│  └─ Your Custom Tables:
│     │
│     ├─ course
│     │  ├─ CourseId (INT, PRIMARY KEY, AUTO_INCREMENT)
│     │  ├─ CourseName (VARCHAR(100))
│     │  └─ CourseZone (VARCHAR(100))
│     │
│     └─ student
│        ├─ StdID (INT, PRIMARY KEY, AUTO_INCREMENT)
│        ├─ StdName (VARCHAR(100))
│        ├─ StdAge (INT)
│        ├─ StdEmail (VARCHAR(254))
│        └─ course_id (INT, FOREIGN KEY → course.CourseId)
```

---

## 🔍 Testing Your Setup

### Test Checklist

1. **Server Running**
   ```
   $ python manage.py runserver
   ✓ Server starts without errors
   ```

2. **Login Works**
   ```
   Visit: http://127.0.0.1:8000/accounts/login/
   ✓ Login page loads
   ✓ Enter credentials
   ✓ Redirects to main page
   ```

3. **Add Student**
   ```
   Fill form on main page
   ✓ Name, Email, Age, Course
   ✓ Click "Add Student"
   ✓ Student appears in table
   ```

4. **View Students**
   ```
   Check student table
   ✓ All fields display correctly
   ✓ Course name shows properly
   ```

5. **Edit Student**
   ```
   Click "Edit" button
   ✓ Edit page loads with current data
   ✓ Modify any field
   ✓ Click "Update Student"
   ✓ Changes saved
   ```

6. **Delete Student**
   ```
   Click "Delete" button
   ✓ Student removed from table
   ✓ Page refreshes
   ```

7. **Admin Panel**
   ```
   Visit: http://127.0.0.1:8000/admin/
   ✓ Admin login works
   ✓ Can see Students and Courses
   ✓ Can add/edit/delete via admin
   ```

---

## ⚠️ Common Issues & Quick Fixes

### Issue 1: "Access denied for user"
```
Problem: MySQL password incorrect
Fix: Update PASSWORD in settings.py
```

### Issue 2: "No module named 'MySQLdb'"
```
Problem: PyMySQL not installed
Fix: pip install pymysql
```

### Issue 3: "Database does not exist"
```
Problem: Database not created
Fix: python setup_database.py
```

### Issue 4: "Table doesn't exist"
```
Problem: Migrations not run
Fix: python manage.py migrate
```

### Issue 5: "Permission denied"
```
Problem: MySQL user lacks permissions
Fix: GRANT ALL PRIVILEGES ON student_management.* TO 'root'@'localhost';
```

---

## 📁 File Organization Reference

```
Where to find things:
├── Settings: student_project/settings.py
├── Models: students/models.py
├── Views: students/views.py
├── URLs: students/urls.py
├── Templates: students/templates/
├── Admin: students/admin.py
└── Database: MySQL (student_management)
```

---

## 🎓 Learning Resources

- Django Documentation: https://docs.djangoproject.com/
- MySQL Documentation: https://dev.mysql.com/doc/
- Bootstrap Documentation: https://getbootstrap.com/docs/

---

## ✅ Success Indicators

You know everything is working when:

✓ Server runs without errors
✓ Can login successfully
✓ Can add students
✓ Can view students
✓ Can edit students
✓ Can delete students
✓ Admin panel accessible
✓ No error messages

---

## 🆘 Getting Help

If stuck:
1. Check CHECKLIST.md
2. Read SETUP_INSTRUCTIONS.txt
3. Review MYSQL_SETUP_GUIDE.md
4. Consult README.md troubleshooting section

---

*Visual Guide v1.0 | April 3, 2026*
