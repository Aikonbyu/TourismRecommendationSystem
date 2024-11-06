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
    columns = [
        "id", "name", "description", "domesticPrice", "foreignPrice", "village", 
        "subDistrict", "district", "userID", "imageURL", "categories", "facilities"
    ]

    connection.close_db(connect, cursor)
    return pd.DataFrame(results, columns=columns)

def get_destinations_by_name(name):
    connect, cursor = connection.connect_db()
    name = name.lower().strip()
    query = """
        SELECT destinations.*, GROUP_CONCAT(DISTINCT categories.name) AS categories,
        GROUP_CONCAT(DISTINCT facilities.name) AS facilities
        FROM destinations
        LEFT JOIN destination_categories ON destinations.id = destination_categories.destinationId
        LEFT JOIN categories ON destination_categories.categoryId = categories.id
        LEFT JOIN destination_facilities ON destinations.id = destination_facilities.destinationId
        LEFT JOIN facilities ON destination_facilities.facilityId = facilities.id
        WHERE LOWER(destinations.name) LIKE %s
        GROUP BY destinations.id
    """
    cursor.execute(query, (f"%{name}%",))
    result = cursor.fetchall()
    columns = [
        "id", "name", "description", "domesticPrice", "foreignPrice", "village", 
        "subDistrict", "district", "userID", "imageURL", "categories", "facilities"
    ]

    connection.close_db(connect, cursor)
    return pd.DataFrame(result, columns=columns)

def get_destination_by_id(id):
    connect, cursor = connection.connect_db()
    query = """
        SELECT name, description, imageURL FROM destinations WHERE id = %s
    """
    cursor.execute(query, (id,))
    result = cursor.fetchall()
    name = result[1]
    description = result[2]
    imageURL = result[9]

    connection.close_db(connect, cursor)
    return name, description, imageURL