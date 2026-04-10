# 📊 Data Storage Guide - Student Management System

## Current Storage Configuration

### ✅ Currently Using: SQLite Database

**Location:** `c:\Users\Admin\OneDrive\Pictures\Desktop\student_mng\db.sqlite3`

---

## 🗄️ Where Your Data Lives

### 1. **SQLite Mode (Current)**
```
📁 Project Root
  └── 📄 db.sqlite3  ← ALL DATA HERE
      ├── student table
      │   ├── StdID
      │   ├── StdName
      │   ├── StdEmail
      │   ├── StdAge
      │   └── course_id (FK)
      │
      └── course table
          ├── CourseId
          ├── CourseName
          └── CourseZone
```

### 2. **MySQL Mode (After Configuration)**
```
🖥️ MySQL Server (localhost:3306)
  └── 📊 Database: student_management
      ├── 📋 Table: student
      │   ├── StdID (Primary Key)
      │   ├── StdName
      │   ├── StdEmail
      │   ├── StdAge
      │   └── course_id (Foreign Key)
      │
      └── 📋 Table: course
          ├── CourseId (Primary Key)
          ├── CourseName
          └── CourseZone
```

---

## 📍 How to Check Your Data

### Method 1: Django Admin Panel
1. Go to: http://127.0.0.1:8000/admin/
2. Login with superuser credentials
3. Click "Students" or "Courses"
4. View all stored data

### Method 2: Database Browser (SQLite)
**For SQLite:**
- Download: [DB Browser for SQLite](https://sqlitebrowser.org/)
- Open file: `db.sqlite3`
- Browse tables: `student`, `course`

**For MySQL:**
- Use: MySQL Workbench or phpMyAdmin
- Connect to localhost:3306
- Database: `student_management`
- Run queries: `SELECT * FROM student;`

### Method 3: Django Shell
```bash
python manage.py shell
```

Then run:
```python
from students.models import Student, Course

# View all students
Student.objects.all()

# View all courses
Course.objects.all()

# Count records
Student.objects.count()
Course.objects.count()
```

---

## 🔄 Switching to MySQL (Production)

### Step 1: Update settings.py
Open: `student_project/settings.py` (line ~82)

Change FROM:
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
```

Change TO:
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'student_management',
        'USER': 'root',
        'PASSWORD': 'your_password',  # ⚠️ ADD YOUR PASSWORD
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
```

### Step 2: Create MySQL Database
```sql
-- In MySQL Workbench or Command Line
CREATE DATABASE student_management;
```

### Step 3: Run Migrations
```bash
python manage.py migrate
```

### Step 4: Transfer Data (Optional)
Export from SQLite and import to MySQL, or start fresh.

---

## 📂 What Gets Stored

### Student Records
| Field | Type | Description |
|-------|------|-------------|
| StdID | INT | Auto-increment primary key |
| StdName | VARCHAR(100) | Student's full name |
| StdEmail | VARCHAR(254) | Email address |
| StdAge | INT | Age in years |
| course_id | INT | Foreign key to course table |

### Course Records
| Field | Type | Description |
|-------|------|-------------|
| CourseId | INT | Auto-increment primary key |
| CourseName | VARCHAR(100) | Course name (e.g., "Computer Science") |
| CourseZone | VARCHAR(100) | Category/zone (auto-set to "General") |

---

## 🔐 Data Persistence

### Current Setup (SQLite)
- ✅ Data persists between server restarts
- ✅ Stored in single file: `db.sqlite3`
- ✅ Easy to backup (just copy the file)
- ⚠️ Not suitable for high-traffic production

### MySQL Setup (Recommended for Production)
- ✅ Data persists in MySQL server
- ✅ Better performance for multiple users
- ✅ Industry-standard security
- ✅ Scalable for large datasets
- ✅ Proper user permissions and access control

---

## 💾 Backup Your Data

### SQLite Backup
```bash
# Simply copy the file
cp db.sqlite3 db.sqlite3.backup
```

### MySQL Backup
```bash
# Export database
mysqldump -u root -p student_management > backup.sql

# Import later
mysql -u root -p student_management < backup.sql
```

---

## 🎯 Quick Verification

### Test if data is being saved:
1. Add a student via: http://127.0.0.1:8000/
2. Check admin panel: http://127.0.0.1:8000/admin/
3. Or use Django shell:
   ```bash
   python manage.py shell
   >>> from students.models import Student
   >>> print(Student.objects.all())
   ```

### Current Database Location:
```
📍 c:\Users\Admin\OneDrive\Pictures\Desktop\student_mng\db.sqlite3
```

All student names, emails, ages, and courses are stored in this file!

---

## 🚀 Mobile Responsiveness Updates

### Recent Improvements:
✅ Optimized for mobile screens (320px - 768px)
✅ Responsive form layouts
✅ Touch-friendly buttons
✅ Horizontal scrolling for tables on small screens
✅ Adaptive font sizes
✅ Compact spacing on mobile devices

### Tested On:
- 📱 iPhone (375px width)
- 📱 Android phones (360px - 412px width)
- 📱 Tablets (768px width)
- 💻 Desktop (1920px width)

---

*Last Updated: April 3, 2026*
*Database: SQLite (db.sqlite3)*
*Ready for MySQL migration*
