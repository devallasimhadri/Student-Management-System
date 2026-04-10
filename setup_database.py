import pymysql
import getpass

print("=" * 60)
print("Student Management System - MySQL Database Setup")
print("=" * 60)
print()

# Get MySQL credentials from user
mysql_user = input("Enter MySQL username (default: root): ").strip() or "root"
mysql_password = getpass.getpass("Enter MySQL password: ")
mysql_host = input("Enter MySQL host (default: localhost): ").strip() or "localhost"
mysql_port = input("Enter MySQL port (default: 3306): ").strip() or "3306"
db_name = input("Enter database name (default: student_management): ").strip() or "student_management"

print()
print("Connecting to MySQL server...")

try:
    # Connect to MySQL server
    connection = pymysql.connect(
        host=mysql_host,
        user=mysql_user,
        password=mysql_password,
        port=int(mysql_port)
    )
    
    print("✓ Connected successfully!")
    
    # Create cursor
    cursor = connection.cursor()
    
    # Create database
    print(f"Creating database '{db_name}'...")
    cursor.execute(f"CREATE DATABASE IF NOT EXISTS {db_name}")
    print(f"✓ Database '{db_name}' created successfully!")
    
    # Commit changes
    connection.commit()
    
    print()
    print("=" * 60)
    print("Database setup completed!")
    print("=" * 60)
    print()
    print("Next steps:")
    print("1. Update student_project/settings.py with your MySQL credentials:")
    print(f"   - USER: '{mysql_user}'")
    print(f"   - PASSWORD: '********' (your password)")
    print(f"   - HOST: '{mysql_host}'")
    print(f"   - PORT: '{mysql_port}'")
    print()
    print("2. Run migrations:")
    print("   python manage.py makemigrations")
    print("   python manage.py migrate")
    print()
    print("3. Create superuser:")
    print("   python manage.py createsuperuser")
    print()
    print("4. Run development server:")
    print("   python manage.py runserver")
    print()
    
except pymysql.err.OperationalError as e:
    print(f"✗ Error: {e}")
    print("Please check your MySQL credentials and try again.")
    
except Exception as e:
    print(f"✗ Unexpected error: {e}")
    
finally:
    # Close connection
    if 'connection' in locals() and connection.open:
        connection.close()
        print("✓ Connection closed")
