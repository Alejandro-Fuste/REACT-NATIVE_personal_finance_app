from pymongo import MongoClient
from environment_variables import mongo_url
from server.entities.user import User
from server.entities.paper_trade import PaperTrade
from faker import Faker

# database connection -------------
connection_string = mongo_url
client = MongoClient(connection_string)
database = client.finance_app
collection = database.users

# Delete old entries before adding new entries
delete_previous_entries = collection.delete_many({})

print(f"{delete_previous_entries.deleted_count} documents deleted.")

# New entries ---------------------
fake = Faker()

#   Paper Trades --------------------
paper_trade_1 = PaperTrade

#   Users  --------------------------

test_user = {'firstName': 'Leia', 'lastName': 'Skywalker'}

# result = collection_name.insert_one(test_user)
#
# print(result.inserted_id)
