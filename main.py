from server.custom_exceptions.duplicate_trade import DuplicateTrade
from server.custom_exceptions.duplicate_user import DuplicateUser
from server.custom_exceptions.email_wrong_format import EmailWrongFormat
from server.custom_exceptions.input_missing import InputMissing
from server.custom_exceptions.input_not_string import InputNotString
from server.custom_exceptions.input_too_long import InputTooLong
from server.custom_exceptions.input_too_short import InputTooShort
from server.custom_exceptions.no_trades import NoTrades
from server.custom_exceptions.paper_trade_exception import PaperTradeException
from server.custom_exceptions.trade_not_found import TradeNotFound
from server.custom_exceptions.user_id_not_provided import MissingUserId
from server.custom_exceptions.user_id_must_be_string import UserIdMustBeString
from server.custom_exceptions.user_not_found import UserNotFound

from server.data_access_layer.implementation_classes.user_dao import UserDAO, UserDAOImp
from server.data_access_layer.implementation_classes.paper_trade_dao import PaperTradeDAO, PaperTradeDAOImp

from server.service_layer.implementation_classes.user_service import UserService, UserServiceImp
from server.service_layer.implementation_classes.paper_trade_service import PaperTradeService, PaperTradeServiceImp

from server.entities.db_user import DatabaseUser
from server.entities.user import User
from server.entities.paper_trade import PaperTrade

from flask import Flask, request, jsonify
from flask_cors import CORS

import logging

logging.basicConfig(filename="records.log", level=logging.DEBUG, format=f"%(asctime)s %(levelname)s %(message)s")

app: Flask = Flask(__name__)
CORS(app)

user_dao: UserDAO = UserDAOImp()
user_service: UserService = UserServiceImp(user_dao)
paper_trade_dao: PaperTradeDAO = PaperTradeDAOImp()
paper_trade_service: PaperTradeService = PaperTradeServiceImp(paper_trade_dao)


@app.route("/")
def on():
    return "Python is running!"


# User Routes ---------------------------------------------------------------------------------------------------------
# Create routes -------
# Read routes -------

@app.get("/api/users")
def get_all_users():
    try:
        data = user_service.get_all_users()
        data_list = []
        dictionary_data = []
        for item in data:
            data_list.append(User(str(item["_id"]), item["firstName"], item["lastName"], item["email"],
                                  item["username"], item["password"], item['paperTrades']))

        for d in data_list:
            dictionary_data.append(d.make_dictionary())
        return jsonify(dictionary_data), 200

    except UserNotFound as e:
        exception_dictionary = {"errorMessage": str(e)}
        exception_json = jsonify(exception_dictionary)
        return exception_json, 404


# Update routes -------
# Delete routes -------

# Paper Trade Routes --------------------------------------------------------------------------------------------------
# Create routes -------
# Read routes -------
# Update routes -------
# Delete routes -------


app.run()
