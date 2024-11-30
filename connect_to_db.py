import os
import psycopg2

# Retrieve credentials from environment variables
DB_HOST = os.getenv('DB_HOST')
DB_PORT = os.getenv('DB_PORT')
DB_NAME = os.getenv('DB_NAME')
DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')
DB_SSLMODE = os.getenv('DB_SSLMODE')

# Connect to the Neon database
try:
    connection = psycopg2.connect(
        host=DB_HOST,
        port=DB_PORT,
        database=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD,
        sslmode=DB_SSLMODE
    )
    cursor = connection.cursor()
    cursor.execute("SELECT 'Connection successful!'")
    print(cursor.fetchone())
except Exception as e:
    print("Error connecting to the database:", e)
finally:
    if 'connection' in locals() and connection:
        connection.close()
