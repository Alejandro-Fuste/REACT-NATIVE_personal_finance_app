from server.config.connection import create_connection

dbname = create_connection()

collection_name = dbname.users

results = collection_name.find()

for result in results:
    print(result)
