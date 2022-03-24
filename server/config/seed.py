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
paper_trade_1 = PaperTrade(1, "T", fake.pyfloat(left_digits=2, right_digits=2, positive=True),
                           "Call", "3/25", "Straddle",
                           fake.pyfloat(left_digits=0, right_digits=2, positive=True),
                           fake.pyfloat(left_digits=0, right_digits=2, positive=True),
                           fake.pyfloat(left_digits=2, right_digits=2, positive=True),
                           fake.pyfloat(left_digits=2, right_digits=2, positive=True),
                           fake.pyfloat(left_digits=2, right_digits=2, positive=True),
                           fake.pyfloat(left_digits=2, right_digits=2, positive=True),
                           fake.pyfloat(left_digits=2, right_digits=2, positive=True),
                           fake.pyfloat(left_digits=2, right_digits=2, positive=True),
                           fake.pyfloat(left_digits=2, right_digits=2, positive=True),
                           fake.pyfloat(left_digits=2, right_digits=2, positive=True),
                           fake.pyfloat(left_digits=2, right_digits=2, positive=True),
                           fake.pyint(max_value=100))

#   Users  --------------------------

test_user_1 = User(0, "Luke", "Skywalker", "luke.skywalker@jedi.com",
                   "Master Luke", fake.sha256(raw_output=False), paper_trade_1.make_dictionary())

test_user_2 = User(fake.uuid4(cast_to=int), "Leia", "Organa", "leia.organa@jedi.net",
                   "Princess Leia", fake.sha256(raw_output=False))

result = collection.insert_one(test_user_1.make_dictionary())

print(result.inserted_id)
