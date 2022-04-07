from abc import ABC, abstractmethod
from typing import List

from server.django_app.api.entities.user import User


class UserService(ABC):

    # Create method -------
    @abstractmethod
    def create_new_user(self, user: User) -> dict:
        pass

    # Read methods -------
    @abstractmethod
    def get_user_by_id(self, user_id: str) -> dict:
        pass

    @abstractmethod
    def get_user_by_username(self, username: str) -> dict:
        pass

    @abstractmethod
    def get_all_users(self) -> List[User]:
        pass

    # Update method -------
    @abstractmethod
    def update_username(self, user_id: str, new_info: str) -> dict:
        pass

    # Delete method -------
    @abstractmethod
    def delete_user(self, user_id: str) -> int:
        pass