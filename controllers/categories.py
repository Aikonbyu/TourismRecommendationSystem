from models import connection
import pandas as pd

def get_all_categories():
    connect, cursor = connection.connect_db()
    cursor.execute("SELECT id, name FROM categories")
    categories = cursor.fetchall()
    connection.close_db(connect, cursor)
    return pd.DataFrame(categories, columns=["id", "name"])

def get_categories_by_name(name):
    connect, cursor = connection.connect_db()
    name = name.lower().strip()
    query = "SELECT id, name FROM categories WHERE LOWER(name) LIKE %s"
    cursor.execute(query, (f"%{name}%",))
    category = cursor.fetchall()
    connection.close_db(connect, cursor)
    return pd.DataFrame(category, columns=["id", "name"])