from abc import ABC, abstractmethod


class UserService(ABC):

    # Create method -------
    @abstractmethod
    def create_new_user(self, user: dict) -> dict:
        pass

    # Read methods -------
    @abstractmethod
    def get_user_by_id(self, user_id: str) -> dict:
        pass

    @abstractmethod
    def get_user_by_username(self, username: str) -> dict:
        pass

    @abstractmethod
    def get_all_users(self) -> list[dict]:
        pass

    # Update method -------
    @abstractmethod
    def update_username(self, user_id: str, new_info: str) -> dict:
        pass

    # Delete method -------
    @abstractmethod
    def delete_user(self, user_id: str) -> int:
        pass
