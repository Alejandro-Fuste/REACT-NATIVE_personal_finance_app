from pymongo import MongoClient
from server.environment_variables import mongo_url


def test_connection():
    try:
        connection_string = mongo_url
        client = MongoClient(connection_string)
        database = client.finance_app

        print(client.list_database_names())
        print(database.list_collection_names())
        print("Able to connect to the database.")

        return database
    except Exception as e:
        print("Unable to connect to the server.")


connection = test_connection()


