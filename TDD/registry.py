class User:
    
    def __init__(self, name):
        self.name = name

    def create_username(self, username):
        return {self.name:username}
