from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse

from .data_access_layer.implementation_classes.user_dao import UserDAOImp
from .service_layer.implementation_classes.user_service import UserServiceImp

user_dao = UserDAOImp()
user_service = UserServiceImp(user_dao)


# Create functions ------------------------------------------------------------
def create_new_user(request):
    pass


# Read functions ------------------------------------------------------------
def get_user_by_id(request):
    pass


def get_user_by_username(request):
    pass


def get_all_users(request):
    pass


# Update functions ------------------------------------------------------------
def update_username(request):
    pass


# Delete functions ------------------------------------------------------------
def delete_user(request):
    pass
