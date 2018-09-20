accounts = {"paul":"kabali"}

def add_account(name, password):
    accounts[name] = password
   

def login(name, password):
    key, value = name, password
    if key in accounts and accounts[key] == value:
        return True

