import sqlite3

conn = sqlite3.connect('db.sqlite3')
cursor = conn.cursor()

# Check existing tables
cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
tables = cursor.fetchall()
print("Existing tables:", tables)

# Find the student table
for table in tables:
    if 'student' in table[0].lower() and 'auth' not in table[0]:
        print(f"\nChecking table: {table[0]}")
        cursor.execute(f"PRAGMA table_info({table[0]})")
        columns = cursor.fetchall()
        print("Columns:", [col[1] for col in columns])
        
        # Add StdPhone column if it doesn't exist
        if 'StdPhone' not in [col[1] for col in columns]:
            cursor.execute(f"ALTER TABLE {table[0]} ADD COLUMN StdPhone VARCHAR(15)")
            print(f"✓ Added StdPhone column to {table[0]}")
        else:
            print(f"✓ StdPhone column already exists in {table[0]}")

conn.commit()
conn.close()
print("\n✅ Database updated successfully!")
