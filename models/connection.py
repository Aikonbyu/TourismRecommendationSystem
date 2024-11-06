from dotenv import load_dotenv
import mysql.connector
import os

def connect_db():
    load_dotenv()
    DB_USERNAME = os.getenv("DB_USERNAME")
    DB_PASSWORD = os.getenv("DB_PASSWORD")
    DB_HOST = os.getenv("DB_HOST")
    DB_PORT = os.getenv("DB_PORT")
    DB_NAME = os.getenv("DB_NAME")

    # Connect to MySQL database
    try:
        print("Connecting to the database...")
        connection = mysql.connector.connect(
            host = DB_HOST,
            user = DB_USERNAME,
            password = DB_PASSWORD,
            port = DB_PORT,
            database = DB_NAME
        )
        print("Database connection successful.")
        cursor = connection.cursor()
    except mysql.connector.Error as err:
        print(f"Error connecting to the database: {err}")
        exit(1)
    return connection, cursor

def close_db(connection, cursor):
    print("Closing database connection...")
    cursor.close()
    connection.close()