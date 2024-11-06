from models import connection
import pandas as pd

def get_all_facilities():
    connect, cursor = connection.connect_db()
    cursor.execute("SELECT id, name FROM facilities")
    facilities = cursor.fetchall()
    connection.close_db(connect, cursor)
    return pd.DataFrame(facilities, columns=["id", "name"])

def get_facilities_by_name(name):
    connect, cursor = connection.connect_db()
    name = name.lower().strip()
    query = "SELECT id, name FROM facilities WHERE LOWER(name) LIKE %s"
    cursor.execute(query, (f"%{name}%",))
    facility = cursor.fetchall()
    connection.close_db(connect, cursor)
    return pd.DataFrame(facility, columns=["id", "name"])