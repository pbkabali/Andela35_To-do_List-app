accounts = {}

def add_account(name, password):
    accounts[name] = password
   

def login(name, password):
    if name in accounts and password in accounts:
        return True

