# Student Management System - Setup Checklist

Use this checklist to ensure everything is properly configured.

## ✅ Pre-Installation Checklist

- [ ] Python 3.8 or higher installed
- [ ] MySQL Server 8.0+ installed and running
- [ ] pip (Python package manager) available
- [ ] Text editor or IDE installed (VS Code, PyCharm, etc.)

## ✅ Installation Checklist

### Step 1: Install Dependencies
- [ ] Navigate to project directory
- [ ] Run: `pip install -r requirements.txt`
- [ ] Verify installation: `pip list | findstr pymysql`
- [ ] Verify installation: `pip list | findstr mysqlclient`

### Step 2: Database Setup
- [ ] Choose setup method:
  - [ ] Option A: Run `python setup_database.py` (Recommended)
  - [ ] Option B: Manual MySQL command
- [ ] Enter MySQL username (default: root)
- [ ] Enter MySQL password
- [ ] Confirm database "student_management" created

### Step 3: Configure Settings
- [ ] Open `student_project/settings.py`
- [ ] Locate DATABASES section (around line 79)
- [ ] Update PASSWORD field with your actual MySQL password
- [ ] Verify HOST is 'localhost'
- [ ] Verify PORT is '3306'
- [ ] Save the file

### Step 4: Database Migrations
- [ ] Run: `python manage.py makemigrations`
- [ ] Check for success message: "No changes detected" or migration files created
- [ ] Run: `python manage.py migrate`
- [ ] Verify all migrations applied successfully

### Step 5: Create Admin User
- [ ] Run: `python manage.py createsuperuser`
- [ ] Enter username
- [ ] Enter email (optional)
- [ ] Enter password (twice)
- [ ] Note: "Superuser created successfully" message

### Step 6: Add Sample Data (Optional)
- [ ] Run: `python manage.py shell < add_sample_courses.py`
- [ ] Verify courses were created
- [ ] Or plan to add courses via admin panel

## ✅ Testing Checklist

### Start Development Server
- [ ] Run: `python manage.py runserver`
- [ ] Verify server started on http://127.0.0.1:8000/
- [ ] No error messages in terminal

### Test Login
- [ ] Navigate to: http://127.0.0.1:8000/accounts/login/
- [ ] Enter superuser credentials
- [ ] Click "Log in"
- [ ] Verify redirect to main page
- [ ] See welcome message with username

### Test Add Student
- [ ] Fill in Name field
- [ ] Fill in Email field
- [ ] Fill in Age field
- [ ] Select Course from dropdown
- [ ] Click "Add Student"
- [ ] Verify student appears in table below

### Test View Students
- [ ] See student table with columns: Name, Email, Course
- [ ] Verify newly added student is displayed
- [ ] Check data matches what was entered

### Test Edit Student
- [ ] Click "Edit" button next to a student
- [ ] Modify any field
- [ ] Click "Update Student"
- [ ] Verify changes saved
- [ ] Verify redirect to main page

### Test Delete Student
- [ ] Click "Delete" button next to a student
- [ ] Verify student removed from table
- [ ] Page refreshes without deleted student

### Test Logout
- [ ] Click "Logout" button
- [ ] Verify redirect to login page
- [ ] Try accessing main page - should require login again

### Test Admin Panel
- [ ] Navigate to: http://127.0.0.1:8000/admin/
- [ ] Login with superuser credentials
- [ ] See "Students" and "Courses" sections
- [ ] Click on "Students" → see list of all students
- [ ] Click on "Courses" → see list of all courses
- [ ] Try adding a course via admin panel
- [ ] Try editing a student via admin panel

## ✅ Verification Checklist

### Database Verification
- [ ] Open MySQL client or Workbench
- [ ] Connect to database
- [ ] Run: `USE student_management;`
- [ ] Run: `SHOW TABLES;`
- [ ] Verify tables exist: student, course, auth_* tables
- [ ] Run: `SELECT * FROM student;`
- [ ] See your added students

### File Structure Verification
- [ ] All required files present:
  - [ ] manage.py
  - [ ] requirements.txt
  - [ ] student_project/settings.py
  - [ ] students/models.py
  - [ ] students/views.py
  - [ ] students/templates/index.html
  - [ ] students/templates/edit.html
  - [ ] students/templates/registration/login.html

### Documentation Verification
- [ ] README.md accessible
- [ ] SETUP_INSTRUCTIONS.txt readable
- [ ] MYSQL_SETUP_GUIDE.md available
- [ ] PROJECT_SUMMARY.md reviewed

## 🔧 Troubleshooting Checklist

### If Database Connection Fails
- [ ] MySQL service is running
- [ ] Username is correct in settings.py
- [ ] Password is correct in settings.py
- [ ] Database name is "student_management"
- [ ] Host is "localhost"
- [ ] Port is "3306"
- [ ] MySQL user has proper permissions

### If Migrations Fail
- [ ] Database exists
- [ ] Database credentials are correct
- [ ] PyMySQL is installed
- [ ] Run: `python manage.py makemigrations students`
- [ ] Run: `python manage.py migrate`

### If Module Not Found Error
- [ ] Virtual environment activated (if using one)
- [ ] Run: `pip install pymysql`
- [ ] Run: `pip install mysqlclient`
- [ ] Verify: `import pymysql` works in Python shell

### If Template Errors
- [ ] Templates folder exists: students/templates/
- [ ] index.html exists
- [ ] edit.html exists
- [ ] registration/login.html exists
- [ ] Check for syntax errors in HTML

### If Static Files Not Loading
- [ ] Bootstrap CDN links are correct
- [ ] Internet connection active (for CDN)
- [ ] Browser console shows no errors

## 📊 Final Verification

### System Ready Indicators
✅ All of these should be TRUE:
- [ ] Server runs without errors
- [ ] Can login successfully
- [ ] Can add students
- [ ] Can view students
- [ ] Can edit students
- [ ] Can delete students
- [ ] Can logout
- [ ] Admin panel accessible
- [ ] Database contains data

### Performance Check
- [ ] Pages load quickly (< 2 seconds)
- [ ] No console errors in browser
- [ ] No tracebacks in terminal
- [ ] Database queries execute fast

## 🎉 Completion Criteria

Your system is fully functional when:

1. ✅ Database is created and connected
2. ✅ All migrations applied successfully
3. ✅ Superuser account created
4. ✅ Can perform all CRUD operations (Create, Read, Update, Delete)
5. ✅ Authentication working properly
6. ✅ Admin panel accessible
7. ✅ No error messages anywhere

## 📝 Notes Section

Use this space to record important information:

**MySQL Username:** ____________________

**MySQL Password:** ____________________

**Database Name:** student_management

**Django Superuser:** ____________________

**Server URL:** http://127.0.0.1:8000/

**Admin URL:** http://127.0.0.1:8000/admin/

---

## Need Help?

If you encounter issues:
1. Check this checklist item by item
2. Review SETUP_INSTRUCTIONS.txt
3. Read MYSQL_SETUP_GUIDE.md
4. Check README.md troubleshooting section

---

*Last Updated: April 3, 2026*
*Version: 1.0*
