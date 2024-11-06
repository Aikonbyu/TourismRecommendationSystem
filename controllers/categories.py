from models import connection

def get_all_categories():
    connect, cursor = connection.connect_db()
    cursor.execute("SELECT id, name FROM categories")
    categories = cursor.fetchall()
    connection.close_db(connect, cursor)
    return categories