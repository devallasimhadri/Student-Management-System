import pymysql

try:
    # Connect to MySQL with password 123456
    connection = pymysql.connect(
        host='localhost',
        user='root',
        password='123456',
        port=3306
    )
    
    cursor = connection.cursor()
    
    # Create database
    cursor.execute("CREATE DATABASE IF NOT EXISTS student_management")
    print("✓ Database 'student_management' created successfully!")
    
    connection.commit()
    connection.close()
    print("✓ Connection closed")
    
except Exception as e:
    print(f"✗ Error: {e}")
