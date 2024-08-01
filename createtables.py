import pymysql
import os
from dotenv import load_dotenv

load_dotenv()

DBNAME = os.getenv('DBNAME')
HOST = os.getenv('HOST')
USERNAME = os.getenv('USERNAME')
PASSWORD = os.getenv('PASSWORD')

connection = pymysql.connect(
    host=HOST,
    user='avnadmin',
    password=PASSWORD,
    database=DBNAME,
    port=18462
)

try:
    with connection.cursor() as cursor:
        # Create Users_main table
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS Users_main (
            user_id INT AUTO_INCREMENT PRIMARY KEY,
            email VARCHAR(120) NOT NULL UNIQUE,
            password VARCHAR(120) NOT NULL,
            unique_link VARCHAR(255) NOT NULL UNIQUE,
            github_username VARCHAR(100) NOT NULL UNIQUE
        );
        """)

        # Create Visits table
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS Visits (
            id INT AUTO_INCREMENT PRIMARY KEY,
            unique_link VARCHAR(200) NOT NULL,
            city VARCHAR(100),
            state VARCHAR(100),
            country VARCHAR(100),
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        );
        """)
        
        connection.commit()
        print("Tables created successfully")
finally:
    connection.close()
