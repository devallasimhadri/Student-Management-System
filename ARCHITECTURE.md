# System Architecture

## Technology Stack

```
┌─────────────────────────────────────────┐
│         PRESENTATION LAYER              │
│  ┌─────────────────────────────────┐   │
│  │   HTML Templates + Bootstrap 5  │   │
│  │   - index.html                  │   │
│  │   - edit.html                   │   │
│  │   - login.html                  │   │
│  └─────────────────────────────────┘   │
└─────────────────────────────────────────┘
                  ↕
┌─────────────────────────────────────────┐
│         APPLICATION LAYER               │
│  ┌─────────────────────────────────┐   │
│  │      Django Views (views.py)    │   │
│  │   - index()                     │   │
│  │   - edit_student()              │   │
│  │   - delete_student()            │   │
│  └─────────────────────────────────┘   │
│  ┌─────────────────────────────────┐   │
│  │   Django Authentication         │   │
│  │   - Login/Logout                │   │
│  │   - @login_required             │   │
│  └─────────────────────────────────┘   │
└─────────────────────────────────────────┘
                  ↕
┌─────────────────────────────────────────┐
│          DATA ACCESS LAYER              │
│  ┌─────────────────────────────────┐   │
│  │      Django Models (ORM)        │   │
│  │   - Student Model               │   │
│  │   - Course Model                │   │
│  └─────────────────────────────────┘   │
│  ┌─────────────────────────────────┐   │
│  │      PyMySQL Connector          │   │
│  └─────────────────────────────────┘   │
└─────────────────────────────────────────┘
                  ↕
┌─────────────────────────────────────────┐
│           DATABASE LAYER                │
│  ┌─────────────────────────────────┐   │
│  │     MySQL Server 8.0+           │   │
│  │   Database: student_management  │   │
│  │   ┌─────────────────────────┐   │   │
│  │   │ Table: student          │   │   │
│  │   │ - StdID (PK)            │   │   │
│  │   │ - StdName               │   │   │
│  │   │ - StdAge                │   │   │
│  │   │ - StdEmail              │   │   │
│  │   │ - course_id (FK)        │   │   │
│  │   └─────────────────────────┘   │   │
│  │   ┌─────────────────────────┐   │   │
│  │   │ Table: course           │   │   │
│  │   │ - CourseId (PK)         │   │   │
│  │   │ - CourseName            │   │   │
│  │   │ - CourseZone            │   │   │
│  │   └─────────────────────────┘   │   │
│  └─────────────────────────────────┘   │
└─────────────────────────────────────────┘
```

## Request Flow

```
User Browser
     │
     │ HTTP Request
     ↓
┌──────────────────────┐
│  Django Server       │
│  (manage.py runserver)│
└──────────────────────┘
     │
     ↓
┌──────────────────────┐
│  URL Routing         │
│  (urls.py)           │
└──────────────────────┘
     │
     ↓
┌──────────────────────┐
│  View Function       │
│  (views.py)          │
└──────────────────────┘
     │
     ├─→ Authentication Check
     │
     ├─→ Query Database (via ORM)
     │
     ├─→ Process Data
     │
     ↓
┌──────────────────────┐
│  Render Template     │
│  (HTML + Bootstrap)  │
└──────────────────────┘
     │
     ↓
HTTP Response
     │
     ↓
User Browser
```

## Database Schema

```
┌─────────────────────────┐
│      student Table      │
├─────────────────────────┤
│ PK  StdID (INT)         │
│     StdName (VARCHAR)   │
│     StdAge (INT)        │
│     StdEmail (VARCHAR)  │
│ FK  course_id (INT) ────┼──┐
└─────────────────────────┘  │
                             │
                             │ Foreign Key Relationship
                             │
                             ↓
                    ┌─────────────────────────┐
                    │      course Table       │
                    ├─────────────────────────┤
                    │ PK  CourseId (INT)      │
                    │     CourseName (VARCHAR)│
                    │     CourseZone (VARCHAR)│
                    └─────────────────────────┘
```

## Entity Relationship

```
Student (1) ────⟨ Belongs To ⟩──── (N) Course

One Course can have Many Students
One Student belongs to One Course
```

## File Structure

```
student_mng/
│
├── manage.py                      # Django management script
├── requirements.txt               # Python dependencies
├── setup_database.py              # Database setup script
├── add_sample_courses.py          # Sample data loader
│
├── student_project/               # Django Project Settings
│   ├── __init__.py
│   ├── settings.py                # Configuration (DB, Apps, etc.)
│   ├── urls.py                    # Main URL routing
│   ├── wsgi.py
│   └── asgi.py
│
├── students/                      # Main Application
│   ├── __init__.py
│   ├── models.py                  # Database models
│   ├── views.py                   # Business logic
│   ├── urls.py                    # App URL routing
│   ├── admin.py                   # Admin panel config
│   ├── apps.py
│   ├── tests.py
│   │
│   ├── templates/
│   │   ├── index.html             # Main dashboard
│   │   ├── edit.html              # Edit student form
│   │   └── registration/
│   │       └── login.html         # Login page
│   │
│   └── migrations/                # Database migrations
│       ├── 0001_initial.py
│       ├── 0002_*.py
│       └── __init__.py
│
└── Documentation/
    ├── README.md
    ├── MYSQL_SETUP_GUIDE.md
    ├── SETUP_INSTRUCTIONS.txt
    ├── PROJECT_SUMMARY.md
    └── ARCHITECTURE.md (this file)
```

## Security Layers

```
┌─────────────────────────────────────┐
│  User Authentication Layer          │
│  - Login required for all views     │
│  - Session management               │
└─────────────────────────────────────┘
              ↓
┌─────────────────────────────────────┐
│  CSRF Protection Layer              │
│  - CSRF tokens on all forms         │
└─────────────────────────────────────┘
              ↓
┌─────────────────────────────────────┐
│  SQL Injection Prevention           │
│  - Django ORM parameterized queries │
└─────────────────────────────────────┘
              ↓
┌─────────────────────────────────────┐
│  Database Access Layer              │
│  - Credential-based access          │
└─────────────────────────────────────┘
```

## Deployment Considerations

### Development (Current)
- Debug: ON
- Database: MySQL Local
- Static Files: Served by Django
- Allowed Hosts: localhost only

### Production (Recommended)
- Debug: OFF
- Database: MySQL Remote (configured properly)
- Static Files: Served by web server (Nginx/Apache)
- Allowed Hosts: Your domain
- HTTPS: Required
- Environment Variables: For sensitive data
- Gunicorn/uWSGI: Application server
- Nginx: Reverse proxy

---

*This architecture ensures separation of concerns, security, and scalability.*
