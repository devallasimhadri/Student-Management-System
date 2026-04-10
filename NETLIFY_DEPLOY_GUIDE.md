# Netlify Deployment Guide - Student Management System

## 🚀 Deploy to Netlify with Permanent Database

### Step 1: Prepare Your Project

All necessary files have been added:
- ✅ `Procfile` - Web server configuration
- ✅ `runtime.txt` - Python version
- ✅ `netlify.toml` - Netlify config
- ✅ Updated `requirements.txt` - Added deployment packages
- ✅ Updated `settings.py` - Environment variables & database config

---

### Step 2: Set Up PostgreSQL Database (Permanent Storage)

**Option A: Neon.tech (Recommended - Free)**
1. Go to: https://neon.tech/
2. Sign up for free account
3. Create new project
4. Copy connection string (looks like: `postgresql://user:pass@host/dbname`)

**Option B: Supabase (Free)**
1. Go to: https://supabase.com/
2. Create new project
3. Get database URL from Settings → Database

**Option C: Railway.app (Free tier)**
1. Go to: https://railway.app/
2. Create PostgreSQL database
3. Copy DATABASE_URL

---

### Step 3: Deploy to Netlify

**Method 1: GitHub Integration (Recommended)**
1. Push your code to GitHub
2. Go to: https://app.netlify.com/
3. Click "Add new site" → "Import an existing project"
4. Connect GitHub and select your repo
5. Build settings auto-detected from `netlify.toml`
6. **IMPORTANT**: Add environment variables (see Step 4)
7. Click "Deploy site"

**Method 2: Drag & Drop**
1. Go to: https://app.netlify.com/drop
2. Drag your entire project folder
3. Configure environment variables
4. Deploy

---

### Step 4: Set Environment Variables on Netlify

Go to: Site Settings → Environment Variables

Add these:

```
DATABASE_URL=postgresql://user:password@host:port/dbname
DJANGO_SECRET_KEY=your-secret-key-here
DJANGO_DEBUG=False
DJANGO_ALLOWED_HOSTS=your-site.netlify.app,localhost
```

**Get your secret key:**
- Keep current one or generate new: https://djecrety.ir/

---

### Step 5: Run Migrations After Deploy

After first deployment:
1. Go to Netlify Dashboard
2. Open "Functions" or use Netlify CLI
3. Run: `python manage.py migrate`
4. Create superuser: `python manage.py createsuperuser`

Or use Netlify's build command to auto-migrate.

---

## 📊 What's Been Added

### New Features:
✅ Mobile phone number field  
✅ Responsive mobile design  
✅ PostgreSQL support (permanent storage)  
✅ WhiteNoise for static files  
✅ Gunicorn web server  
✅ Environment variable configuration  

### Database Options:
- **SQLite**: Local development (current)
- **PostgreSQL**: Production on Netlify (permanent)
- **MySQL**: Can be configured if needed

---

## 🔧 Local Testing Before Deploy

Install new dependencies:
```bash
pip install -r requirements.txt
```

Test with PostgreSQL locally:
```bash
# Set environment variable
set DATABASE_URL=postgresql://user:pass@localhost/dbname

# Run migrations
python manage.py migrate

# Test server
python manage.py runserver
```

---

## 📱 Mobile Number Field

Added to all forms:
- ✅ Add student form
- ✅ Edit student form  
- ✅ Display in table
- ✅ Optional field (can be blank)
- ✅ Stored permanently in database

---

## 💾 Data Persistence

**With SQLite (Current):**
- Data stored in `db.sqlite3` file
- Persists until you delete the file
- Not suitable for Netlify (ephemeral filesystem)

**With PostgreSQL (Netlify):**
- Data stored in cloud database
- Permanent until you delete it
- Survives redeployments
- Professional-grade reliability

---

## ⚠️ Important Notes

1. **Database URL is Required**: Netlify needs `DATABASE_URL` env var
2. **Static Files**: Collected automatically during build
3. **Migrations**: Must run after first deploy
4. **Secret Key**: Change in production for security
5. **Debug Mode**: Set to False on Netlify

---

## 🎯 Quick Deploy Checklist

- [ ] Code pushed to GitHub
- [ ] PostgreSQL database created
- [ ] DATABASE_URL copied
- [ ] Netlify account created
- [ ] Site connected to GitHub repo
- [ ] Environment variables set
- [ ] First deployment successful
- [ ] Migrations run
- [ ] Superuser created
- [ ] Site tested and working

---

## 🆘 Troubleshooting

**Build Fails:**
- Check build logs on Netlify
- Verify `requirements.txt` has all packages
- Ensure Python version matches

**Database Connection Error:**
- Verify DATABASE_URL format
- Check database allows connections
- Ensure SSL is configured if required

**Static Files Not Loading:**
- WhiteNoise middleware is configured
- STATIC_ROOT is set correctly
- collectstatic ran successfully

---

*Ready to deploy! Follow the steps above and your app will be live on Netlify with permanent data storage.*
