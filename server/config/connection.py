from pymongo import MongoClient
from environment_variables import mongo_url
import os


def test_connection():
    try:
        connection_string = mongo_url
        # connection_string: str = os.environ.get("MongoURL")
        client = MongoClient(connection_string)
        database = client.finance_app

        print(client.list_database_names())
        print(database.list_collection_names())
        print("Able to connect to the database.")

        return database
    except Exception as e:
        print("Unable to connect to the server.")


connection = test_connection()


