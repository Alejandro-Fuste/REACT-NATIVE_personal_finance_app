from django.urls import path
from . import views

# URLConf
urlpatterns = [
    path('', views.create_new_user()),
    path('', views.get_user_by_id()),
    path('', views.get_user_by_username()),
    path('', views.get_all_users()),
    path('', views.update_username()),
    path('', views.delete_user())
]
