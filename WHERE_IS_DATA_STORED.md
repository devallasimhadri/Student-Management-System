# 📍 WHERE YOUR DATA IS STORED - Step by Step Guide

## ✅ Current Data Storage Location

### All your data is stored in ONE file:

```
📁 c:\Users\Admin\OneDrive\Pictures\Desktop\student_mng\db.sqlite3
```

---

## 🔍 How to See Your Data (5 Methods)

### Method 1: Django Admin Panel (EASIEST) ⭐

**Step 1:** Open browser  
**Step 2:** Go to: `http://127.0.0.1:8000/admin/`  
**Step 3:** Login with your username and password  
**Step 4:** Click **"Students"** under STUDENTS section  
**Step 5:** See ALL student records including phone numbers!  
**Step 6:** Click **"Courses"** to see all courses  

✅ **You can view, edit, add, or delete data here!**

---

### Method 2: File Explorer (See the Database File)

**Step 1:** Press `Windows + E` to open File Explorer  
**Step 2:** Navigate to this path:
```
c:\Users\Admin\OneDrive\Pictures\Desktop\student_mng\
```
**Step 3:** Look for file named: **`db.sqlite3`**  
**Step 4:** This file contains EVERYTHING:
   - All student names
   - All email addresses
   - All ages
   - All phone numbers ✨
   - All course names
   - User accounts
   - Sessions

**Step 5:** Right-click the file → Properties  
**Step 6:** See file size (shows how much data you have)

⚠️ You can't read it directly - need special software (see Method 3)

---

### Method 3: DB Browser for SQLite (Visual Viewer) 🎯

**Step 1:** Download free tool: https://sqlitebrowser.org/dl/  
**Step 2:** Install and open "DB Browser for SQLite"  
**Step 3:** Click "Open Database" button  
**Step 4:** Browse to:
```
c:\Users\Admin\OneDrive\Pictures\Desktop\student_mng\db.sqlite3
```
**Step 5:** Click "Open"  
**Step 6:** Click "Browse Data" tab at top  
**Step 7:** Select table from dropdown:
   - Choose `student_student` → See all students with phones
   - Choose `student_course` → See all courses

✅ **Best way to see raw database visually!**

---

### Method 4: Main Website (View Students)

**Step 1:** Open browser  
**Step 2:** Go to: `http://127.0.0.1:8000/`  
**Step 3:** Login if prompted  
**Step 4:** Scroll down to "Student List" table  
**Step 5:** See all students displayed with:
   - Name
   - Email
   - Age
   - **Phone Number** ✨
   - Course

---

### Method 5: Command Line (Advanced)

**Step 1:** Open terminal/command prompt  
**Step 2:** Navigate to project folder:
```bash
cd c:\Users\Admin\OneDrive\Pictures\Desktop\student_mng
```
**Step 3:** Run Django shell:
```bash
python manage.py shell
```
**Step 4:** Type these commands:

To see all students:
```python
from students.models import Student
students = Student.objects.all()
for s in students:
    print(f"{s.StdName} | {s.StdEmail} | {s.StdPhone}")
```

To count records:
```python
print(f"Total Students: {Student.objects.count()}")
print(f"Total Courses: {Course.objects.count()}")
```

**Step 5:** Press `Ctrl+Z` then `Enter` to exit

---

## 📊 What's Stored in Database

### Table: `student_student`
Contains all student records:
- `StdID` - Unique ID number
- `StdName` - Student's name
- `StdEmail` - Email address
- `StdAge` - Age in years
- **`StdPhone` - Phone number** ✨ NEW!
- `course_id` - Links to course

### Table: `student_course`
Contains all courses:
- `CourseId` - Unique ID
- `CourseName` - Course name (e.g., "Computer Science")
- `CourseZone` - Category (default: "General")

---

## 💾 Backup Your Data

**To backup all your data:**

**Step 1:** Close the server (Ctrl+C in terminal)  
**Step 2:** Copy the file:
```
Copy: db.sqlite3
```
**Step 3:** Paste it somewhere safe:
```
Paste as: db_backup_2026.sqlite3
```

That's it! Your entire database is backed up!

---

## 🗑️ To Delete All Data

**Option 1: Delete specific students**
- Go to admin panel: http://127.0.0.1:8000/admin/
- Select students → Delete

**Option 2: Delete entire database**
- Close server
- Delete file: `db.sqlite3`
- Run: `python manage.py migrate` (creates fresh empty database)

---

## ☁️ After Netlify Deployment

When you deploy to Netlify with PostgreSQL:

**Data will be stored in:**
```
☁️ Cloud Database (Neon.tech / Supabase)
```

**Benefits:**
- ✅ Permanent storage
- ✅ Accessible from anywhere
- ✅ Survives redeployments
- ✅ Professional reliability
- ✅ Data stays until YOU delete it

**To see data after deployment:**
- Use Django Admin panel (same as before)
- Or connect to PostgreSQL with database tool

---

## 🎯 Quick Summary

| What | Where |
|------|-------|
| **Database File** | `db.sqlite3` |
| **Location** | Project folder |
| **Full Path** | `c:\Users\Admin\OneDrive\Pictures\Desktop\student_mng\db.sqlite3` |
| **Contains** | Students, Courses, Users |
| **Phone Numbers** | Yes! In `student_student` table |
| **Backup** | Just copy the file |
| **View Easily** | Admin panel or DB Browser |

---

## 🚀 Test It Now!

1. **Add a student** with phone number at: http://127.0.0.1:8000/
2. **View it** in admin panel: http://127.0.0.1:8000/admin/
3. **See the file** in File Explorer
4. **Open with DB Browser** to see raw data

Your phone numbers are now being saved permanently! 📱✨
