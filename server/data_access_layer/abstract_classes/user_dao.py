from abc import ABC, abstractmethod
from typing import List

from server.entities.user import User


class UserDAO(ABC):

    # Create method -------
    @abstractmethod
    def create_new_user(self, user: User) -> User:
        pass

    # Read methods -------
    @abstractmethod
    def get_user(self, user_id: int) -> User:
        pass

    @abstractmethod
    def get_all_users(self) -> List[User]:
        pass

    # Update method -------
    @abstractmethod
    def update_user(self, user_id: int, user: User) -> User:
        pass
    
    # Delete method -------
    @abstractmethod
    def delete_user(self, user_id: int) -> bool:
        pass
