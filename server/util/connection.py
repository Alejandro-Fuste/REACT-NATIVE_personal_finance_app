import pymongo
import os
from pprint import pprint

conn_str: str = os.environ.get("MongoURL")

# set a 5-second connection timeout
client = pymongo.MongoClient(conn_str)

try:
    pprint(client.server_info())
except Exception:
    pprint("Unable to connect to the server.")


