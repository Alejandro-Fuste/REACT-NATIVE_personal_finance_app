import connection

users = connection.users

test_user = {'firstName': 'Luke', 'lastName': 'Skywalker'}

result = db.users.insert_one(test_user)

print(result.inserted_id)
