from connection import create_connection

dbname = create_connection()

collection_name = dbname.users

# delete_previous_entries = collection_name.delete_many({})
#
# print(delete_previous_entries.deleted_count, "documents deleted.")

test_user = {'firstName': 'Leia', 'lastName': 'Skywalker'}

result = collection_name.insert_one(test_user)

print(result.inserted_id)
