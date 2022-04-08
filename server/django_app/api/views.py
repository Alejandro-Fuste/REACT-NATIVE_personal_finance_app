from django.http import JsonResponse

from server.data_access_layer.implementation_classes import UserDAOImp
from .service_layer.implementation_classes.user_service import UserServiceImp

user_dao = UserDAOImp()
user_service = UserServiceImp(user_dao)


# User Controllers -----------------------------------------------------------------------------------------------------

# Create functions ------------------------------------------------------------
def create_new_user(request):
    pass


# Read functions ------------------------------------------------------------
def get_user_by_id(request):
    pass


def get_user_by_username(request):
    pass


def get_all_users(request):
    users: list = user_service.get_all_users()
    data: list = []
    for user in users:
        dictionary_user = user.make_dictionary()
        data.append(dictionary_user)

    return JsonResponse(data, safe=False, status=200)


# Update functions ------------------------------------------------------------
def update_username(request):
    pass


# Delete functions ------------------------------------------------------------
def delete_user(request):
    pass


# Paper Trade Controllers ----------------------------------------------------------------------------------------------

# Create functions ------------------------------------------------------------
def add_paper_trade(request):
    pass


# Read functions ------------------------------------------------------------
def get_paper_trades(request):
    pass


# Update functions ------------------------------------------------------------
def update_paper_trade_sell_price(request):
    pass


# Delete functions ------------------------------------------------------------
def delete_paper_trade(request):
    pass
