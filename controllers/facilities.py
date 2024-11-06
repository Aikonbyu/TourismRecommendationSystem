from models import connection

def get_all_facilities():
    connect, cursor = connection.connect_db()
    cursor.execute("SELECT id, name FROM facilities")
    facilities = cursor.fetchall()
    connection.close_db(connect, cursor)
    return facilities