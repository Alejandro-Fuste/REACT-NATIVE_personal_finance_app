from pymongo import MongoClient
from environment_variables import mongo_url
from server.entities.user import User
from server.entities.paper_trade import PaperTrade
from faker import Faker

# database connection ----------------
connection_string = mongo_url
client = MongoClient(connection_string)
database = client.finance_app
collection = database.users

# delete_previous_entries = collection_name.delete_many({})
#
# print(delete_previous_entries.deleted_count, "documents deleted.")

fake = Faker()

# Paper Trades --------------------

# Users  --------------------------

test_user = {'firstName': 'Leia', 'lastName': 'Skywalker'}

# result = collection_name.insert_one(test_user)
#
# print(result.inserted_id)
