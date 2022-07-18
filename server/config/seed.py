from pymongo import MongoClient
from server.environment_variables import mongo_url
from server.entities.db_user import DatabaseUser
from server.entities.option import Option
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
option_1 = Option("T", fake.pyfloat(left_digits=2, right_digits=2, positive=True),
                  fake.pyfloat(left_digits=0, right_digits=2, positive=True),
                  "5/5", 1, "straddle",
                  fake.pyfloat(left_digits=0, right_digits=2, positive=True),
                  fake.pyfloat(left_digits=2, right_digits=2, positive=True))

option_2 = Option("T", fake.pyfloat(left_digits=2, right_digits=2, positive=True),
                  fake.pyfloat(left_digits=0, right_digits=2, positive=True),
                  "5/5", 1, "straddle",
                  fake.pyfloat(left_digits=0, right_digits=2, positive=True),
                  fake.pyfloat(left_digits=2, right_digits=2, positive=True))

option_3 = Option("T", fake.pyfloat(left_digits=2, right_digits=2, positive=True),
                  fake.pyfloat(left_digits=0, right_digits=2, positive=True),
                  "5/5", 1, "straddle",
                  fake.pyfloat(left_digits=0, right_digits=2, positive=True),
                  fake.pyfloat(left_digits=2, right_digits=2, positive=True))

option_4 = Option("T", fake.pyfloat(left_digits=2, right_digits=2, positive=True),
                  fake.pyfloat(left_digits=0, right_digits=2, positive=True),
                  "5/5", 1, "straddle",
                  fake.pyfloat(left_digits=0, right_digits=2, positive=True),
                  fake.pyfloat(left_digits=2, right_digits=2, positive=True))

#   Users  --------------------------

test_user_1 = DatabaseUser("Luke", "Skywalker", "luke.skywalker@jedi.com",
                           "Master Luke", fake.sha256(raw_output=False), [option_1.make_dictionary(),
                                                                          option_2.make_dictionary()])

test_user_2 = DatabaseUser("Leia", "Organa", "leia.organa@jedi.net",
                           "Princess Leia", fake.sha256(raw_output=False), [option_3.make_dictionary(),
                                                                            option_4.make_dictionary()])

test_user_3 = DatabaseUser("Rey", "Skywalker", "rey.skywalker@jedi.com", "Jedi Knight", fake.sha256(raw_output=False))

#   Add users to database  ----------

result = collection.insert_many([test_user_1.make_dictionary(), test_user_2.make_dictionary(),
                                 test_user_3.make_dictionary()])

for x in collection.find():
    print(x)
