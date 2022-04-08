class User:
    def __init__(self,
                 _id: str = None,
                 first_name: str = None,
                 last_name: str = None,
                 email: str = None,
                 username: str = None,
                 password: str = None,
                 paper_trades: list = []
                 ):
        self._id = str(_id)
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.username = username
        self.password = password
        self.paper_trades = paper_trades

    def make_dictionary(self):
        dictionary = {
            "_id": self._id,
            "firstName": self.first_name,
            "lastName": self.last_name,
            "email": self.email,
            "username": self.username,
            "password": "*****",
            "paperTrades": self.paper_trades
        }
        return dictionary

    def __str__(self):
        return f"_id: {self._id}, first_name: {self.first_name}, last_name: {self.last_name}, " \
               f"email: {self.email}, username: {self.username}, passcode: *****, " \
               f"paper_trade: {self.paper_trades}"

