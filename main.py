import logging

from flask import Flask, request, jsonify
from flask_cors import CORS

logging.basicConfig(filename="records.log", level=logging.DEBUG,
                    format="[%(levelname)s] - %(asctime)s - %(name)s - : %(message)s in %(pathname)s:%(lineno)d")

app: Flask = Flask(__name__)
CORS(app)


@app.route("/")
def hello_world():
    return "Hello, cross-origin-world!"


# data_list = []
# dictionary_data = []
# for item in data:
#     data_list.append(User(str(item["_id"]), item["firstName"], item["lastName"], item["email"],
#                           item["username"], item["password"], item['paperTrades']))
#
# for d in data_list:
#     dictionary_data.append(d.make_dictionary())
# return dictionary_data

app.run()
