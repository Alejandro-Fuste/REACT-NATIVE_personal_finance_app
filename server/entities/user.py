class User:
    def __init__(self,
                 user_id: int = None,
                 first_name: str = None,
                 last_name: str = None,
                 email: str = None,
                 username: str = None,
                 password: str = None,
                 paper_trade: dict = {}
                 ):
        self.user_id = user_id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.username = username
        self.password = password
        self.paper_trade = paper_trade

    def make_dictionary(self):
        dictionary = {
            "userId": self.user_id,
            "firstName": self.first_name,
            "lastName": self.last_name,
            "email": self.email,
            "username": self.username,
            "password": self.password,
            "paperTrade": self.paper_trade
        }
        return dictionary

    def __str__(self):
        return f"user_id: {self.user_id}, first_name: {self.first_name}, last_name: {self.last_name}, " \
               f"email: {self.email}, username: {self.username}, passcode: ********, paper_trade: {self.paper_trade}"

