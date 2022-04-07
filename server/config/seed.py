from pymongo import MongoClient
from server.django_app.finance_app.dao_sample.environment_variables import mongo_url
from server.django_app.api.entities.user import User
from server.django_app.api.entities.paper_trade import PaperTrade
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
paper_trade_1 = PaperTrade(fake.pyint(max_value=10000), "T", fake.pyfloat(left_digits=2, right_digits=2, positive=True),
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

paper_trade_2 = PaperTrade(fake.pyint(max_value=10000), "T", fake.pyfloat(left_digits=2, right_digits=2, positive=True),
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

paper_trade_3 = PaperTrade(fake.pyint(max_value=10000), "T", fake.pyfloat(left_digits=2, right_digits=2, positive=True),
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

paper_trade_4 = PaperTrade(fake.pyint(max_value=10000), "T", fake.pyfloat(left_digits=2, right_digits=2, positive=True),
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

test_user_1 = User(None, "Luke", "Skywalker", "luke.skywalker@jedi.com",
                   "Master Luke", fake.sha256(raw_output=False), [paper_trade_1.make_dictionary(),
                                                                  paper_trade_2.make_dictionary()])

test_user_2 = User(None, "Leia", "Organa", "leia.organa@jedi.net",
                   "Princess Leia", fake.sha256(raw_output=False), [paper_trade_3.make_dictionary(),
                                                                    paper_trade_4.make_dictionary()])

test_user_3 = User(None, "Rey", "Skywalker", "rey.skywalker@jedi.com", "Jedi Knight", fake.sha256(raw_output=False))

#   Add users to database  ----------

result = collection.insert_many([test_user_1.make_dictionary(), test_user_2.make_dictionary(),
                                 test_user_3.make_dictionary()])

for x in collection.find():
    print(x)
