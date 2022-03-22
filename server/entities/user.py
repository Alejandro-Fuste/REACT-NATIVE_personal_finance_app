class User:
    def __init__(self,
                 user_id: int = None,

                 ):
        self.user_id = user_id

    def make_dictionary(self):
        dictionary = {
            "userId": self.user_id,
        }
        return dictionary

    def __str__(self):
        return f"user_id: {self.user_id}"
    