from server.custom_exceptions.user_id_must_be_string import UserIdMustBeString
from server.custom_exceptions.user_id_not_provided import MissingUserId
from server.custom_exceptions.input_not_string import InputNotString
from server.custom_exceptions.input_missing import InputMissing
from server.custom_exceptions.input_too_short import InputTooShort
from server.custom_exceptions.input_too_long import InputTooLong
from server.custom_exceptions.email_wrong_format import EmailWrongFormat

from server.data_access_layer.abstract_classes.user_dao import UserDAO
from server.data_access_layer.implementation_classes.user_dao import UserDAOImp

from server.service_layer.implementation_classes.user_service import UserService, UserServiceImp

user_dao: UserDAO = UserDAOImp()
user_service: UserService = UserServiceImp(user_dao)

user_id_must_be_string: str = "The user id must be a string."
user_id_not_provided: str = "A user id must be provided."
input_must_be_string: str = "The input must be a string."
input_not_provided: str = "An input must be provided."
input_too_short: str = "The input is too short."
input_too_long: str = "The input is too long."
email_wrong_format: str = "The email is not in the correct format."


# Creation Tests ----------------------------------------------------------------------------
# First name not string
def test_create_user_first_name_not_string(create_new_user_first_name_number):
    try:
        user_service.create_new_user(create_new_user_first_name_number)
        assert False
    except InputNotString as e:
        assert str(e) == input_must_be_string


# First name missing
def test_create_user_first_name_missing(create_new_user_first_name_blank):
    try:
        user_service.create_new_user(create_new_user_first_name_blank)
        assert False
    except InputMissing as e:
        assert str(e) == input_not_provided


# First name too short
def test_create_user_first_name_too_short(create_new_user_first_name_too_short):
    try:
        user_service.create_new_user(create_new_user_first_name_too_short)
        assert False
    except InputTooShort as e:
        assert str(e) == input_too_short


# First name too long
def test_create_user_first_name_too_long(create_new_user_first_name_too_long):
    try:
        user_service.create_new_user(create_new_user_first_name_too_long)
        assert False
    except InputTooLong as e:
        assert str(e) == input_too_long


# Last name not string
def test_create_user_last_name_not_string(create_new_user_last_name_number):
    try:
        user_service.create_new_user(create_new_user_last_name_number)
        assert False
    except InputNotString as e:
        assert str(e) == input_must_be_string


# Last name missing
def test_create_user_last_name_missing():
    try:
        user_service.create_new_user()
        assert False
    except InputMissing as e:
        assert str(e) == input_not_provided


# Last name too short
def test_create_user_last_name_too_short():
    try:
        user_service.create_new_user()
        assert False
    except InputTooShort as e:
        assert str(e) == input_too_short


# Last name too long
def test_create_user_last_name_too_long():
    try:
        user_service.create_new_user()
        assert False
    except InputTooLong as e:
        assert str(e) == input_too_long


# Email wrong format
def test_create_user_email_wrong_format(create_new_user_username_number):
    try:
        user_service.create_new_user(create_new_user_username_number)
        assert False
    except EmailWrongFormat as e:
        assert str(e) == email_wrong_format


# Email missing
def test_create_user_email_missing():
    try:
        user_service.create_new_user()
        assert False
    except InputMissing as e:
        assert str(e) == input_not_provided


# username not string
def test_create_user_username_not_string():
    try:
        user_service.create_new_user()
        assert False
    except InputNotString as e:
        assert str(e) == input_must_be_string


# username missing
def test_create_user_username_missing():
    try:
        user_service.create_new_user()
        assert False
    except InputMissing as e:
        assert str(e) == input_not_provided


# username too short
def test_create_user_username_too_short():
    try:
        user_service.create_new_user()
        assert False
    except InputTooShort as e:
        assert str(e) == input_too_short


# username too long
def test_create_user_username_too_long():
    try:
        user_service.create_new_user()
        assert False
    except InputTooLong as e:
        assert str(e) == input_too_long


# Password not string
def test_create_user_password_not_string():
    try:
        user_service.create_new_user()
        assert False
    except InputNotString as e:
        assert str(e) == input_must_be_string


# Password missing
def test_create_user_password_missing():
    try:
        user_service.create_new_user()
        assert False
    except InputMissing as e:
        assert str(e) == input_not_provided


# Password too short
def test_create_user_password_too_short():
    try:
        user_service.create_new_user()
        assert False
    except InputTooShort as e:
        assert str(e) == input_too_short


# Password too long
def test_create_user_password_too_long():
    try:
        user_service.create_new_user()
        assert False
    except InputTooLong as e:
        assert str(e) == input_too_long


# Read Tests --------------------------------------------------------------------------------

def test_get_user_by_id_not_string(invalid_id):
    try:
        user_service.get_user_by_id(invalid_id)
        assert False
    except UserIdMustBeString as e:
        assert str(e) == user_id_must_be_string


def test_get_user_by_id_no_id(missing_id):
    try:
        user_service.get_user_by_id(missing_id)
        assert False
    except MissingUserId as e:
        assert str(e) == user_id_not_provided


# Update Tests --------------------------------------------------------------------------------
# User Id not string
def test_update_username_id_not_string(invalid_id, update_username):
    try:
        user_service.update_username(invalid_id, update_username)
        assert False
    except UserIdMustBeString as e:
        assert str(e) == user_id_must_be_string


# User Id missing
def test_update_username_by_id_no_id(missing_id, update_username):
    try:
        user_service.update_username(missing_id, update_username)
        assert False
    except MissingUserId as e:
        assert str(e) == user_id_not_provided


# Username not string
def test_update_username_not_string(bad_id, bad_username_number):
    try:
        user_service.update_username(bad_id, bad_username_number)
        assert False
    except InputNotString as e:
        assert str(e) == input_must_be_string


# Username missing
def test_update_username_missing(bad_id, username_missing):
    try:
        user_service.update_username(bad_id, username_missing)
        assert False
    except InputMissing as e:
        assert str(e) == input_not_provided


# Username too short
def test_update_username_too_short(bad_id, username_too_short):
    try:
        user_service.update_username(bad_id, username_too_short)
        assert False
    except InputTooShort as e:
        assert str(e) == input_too_short


# Username too long
def test_update_username_too_long(bad_id, username_too_long):
    try:
        user_service.update_username(bad_id, username_too_long)
        assert False
    except InputTooLong as e:
        assert str(e) == input_too_long


# Delete Tests --------------------------------------------------------------------------------

def test_delete_user_by_id_not_string(invalid_id):
    try:
        user_service.delete_user(invalid_id)
        assert False
    except UserIdMustBeString as e:
        assert str(e) == user_id_must_be_string


def test_delete_user_by_id_no_id(missing_id):
    try:
        user_service.delete_user(missing_id)
        assert False
    except MissingUserId as e:
        assert str(e) == user_id_not_provided
