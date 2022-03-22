from pymongo import MongoClient
import os


def create_connection():
    try:
        connection_string: str = os.environ.get("MongoURL")
        client = MongoClient(connection_string)

        return client.finance_app
    except Exception:
        print("Unable to connect to the server.")


if __name__ == "__main__":
    dbname = create_connection()

    collection_name = dbname.users

    test_user = {'firstName': 'Leia', 'lastName': 'Skywalker'}

    result = collection_name.insert_one(test_user)

    print(result.inserted_id)


