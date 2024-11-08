from models import connection
import pandas as pd

def get_all_users():
    connect, cursor = connection.connect_db()
    cursor.execute("SELECT id, username, email FROM users")
    users = cursor.fetchall()
    connection.close_db(connect, cursor)
    return pd.DataFrame(users, columns=["id", "username", "email"])

def get_user_by_name_password(name, password):
    connect, cursor = connection.connect_db()
    query = "SELECT * FROM users WHERE username = %s AND password = %s"
    cursor.execute(query, (name, password))
    user = cursor.fetchall()
    id = None
    if user:
        id = user[0]
    connection.close_db(connect, cursor)
    return id, user

def get_user_by_name(name):
    connect, cursor = connection.connect_db()
    name = name.lower().strip()
    query = "SELECT id, username, email FROM users WHERE LOWER(username) LIKE %s"
    cursor.execute(query, (f"%{name}%",))
    user = cursor.fetchall()
    connection.close_db(connect, cursor)
    return pd.DataFrame(user, columns=["id", "username", "email"])