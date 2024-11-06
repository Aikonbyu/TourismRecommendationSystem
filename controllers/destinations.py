from models import connection
import pandas as pd

def get_destinations_data():
    connect, cursor = connection.connect_db()
    query = """
        SELECT destinations.*, GROUP_CONCAT(DISTINCT categories.name) AS categories,
        GROUP_CONCAT(DISTINCT facilities.name) AS facilities
        FROM destinations
        LEFT JOIN destination_categories ON destinations.id = destination_categories.destinationId
        LEFT JOIN categories ON destination_categories.categoryId = categories.id
        LEFT JOIN destination_facilities ON destinations.id = destination_facilities.destinationId
        LEFT JOIN facilities ON destination_facilities.facilityId = facilities.id
        GROUP BY destinations.id
    """
    cursor.execute(query)
    results = cursor.fetchall()
    connection.close_db(connect, cursor)
    return pd.DataFrame(results)