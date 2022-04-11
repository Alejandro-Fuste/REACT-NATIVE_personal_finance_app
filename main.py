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

# logging.basicConfig(filename="records.log", level=logging.DEBUG, format=f"%(asctime)s %(levelname)s %(message)s")

logging.basicConfig(filename="records.log", level=logging.DEBUG,
                    format="[%(levelname)s] - %(asctime)s - %(name)s - : %(message)s in %(pathname)s:%(lineno)d")

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
@app.post("/api/createUser")
def create_user():
    try:
        data = request.get_json()
        new_user = DatabaseUser(data["firstName"], data["lastName"], data["email"], data["username"], data["password"])
        user_to_return = user_service.create_new_user(new_user.make_dictionary())
        new_user_id = str(user_to_return.inserted_id)

        return jsonify(new_user_id), 201

    except DuplicateUser as e:
        exception_dictionary = {"errorMessage": str(e)}
        exception_json = jsonify(exception_dictionary)
        return exception_json, 400


# Read routes -------

@app.get("/api/user/<user_id>")
def get_user_by_id(user_id):
    try:
        data = user_service.get_user_by_id(user_id)
        user = User(str(data["_id"]), data["firstName"], data["lastName"], data["email"],
                    data["username"], data["password"], data['paperTrades'])

        return jsonify(user.make_dictionary()), 200
    except UserNotFound as e:
        exception_dictionary = {"errorMessage": str(e)}
        exception_json = jsonify(exception_dictionary)
        return exception_json, 400


@app.get("/api/user/username/<username>")
def get_user_by_username(username):
    try:
        data = user_service.get_user_by_username(username)
        user = User(str(data["_id"]), data["firstName"], data["lastName"], data["email"],
                    data["username"], data["password"], data['paperTrades'])

        return jsonify(user.make_dictionary()), 200
    except UserNotFound as e:
        exception_dictionary = {"errorMessage": str(e)}
        exception_json = jsonify(exception_dictionary)
        return exception_json, 400


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

@app.post("/api/createPaperTrade/<user_id>")
def create_paper_trade(user_id):
    try:
        data = request.get_json()
        new_trade = PaperTrade(data["tradeId"], data["ticker"], data["strikePrice"], data["tradeType"],
                               data["expirationDate"], data["strategyType"], data["callPrice"], data["putPrice"],
                               data["callBreakevenPoint"], data["putBreakevenPoint"], data["straddleCallBreakevenPoint"]
                               , data["straddlePutBreakevenPoint"], data["sellPrice"], data["costPrice"],
                               data["totalSell"], data["totalCost"], data["netProfit"], data["netProfitPercentage"])
        trade_to_return = paper_trade_service.add_paper_trade(str(user_id), new_trade.make_dictionary())
        return jsonify(trade_to_return.modified_count), 201

    except DuplicateTrade as e:
        exception_dictionary = {"errorMessage": str(e)}
        exception_json = jsonify(exception_dictionary)
        return exception_json, 400


# Read routes -------

@app.get("/api/paperTrades/<user_id>")
def get_paper_trades(user_id):
    try:
        data = paper_trade_service.get_paper_trades(user_id)
        return jsonify(data), 200
    except UserIdMustBeString as e:
        exception_dictionary = {"errorMessage": str(e)}
        exception_json = jsonify(exception_dictionary)
        return exception_json, 400
    except MissingUserId as e:
        exception_dictionary = {"errorMessage": str(e)}
        exception_json = jsonify(exception_dictionary)
        return exception_json, 400
    except NoTrades as e:
        exception_dictionary = {"errorMessage": str(e)}
        exception_json = jsonify(exception_dictionary)
        return exception_json, 400
    except UserNotFound as e:
        exception_dictionary = {"errorMessage": str(e)}
        exception_json = jsonify(exception_dictionary)
        return exception_json, 400


# Update routes -------
# Delete routes -------


app.run()
