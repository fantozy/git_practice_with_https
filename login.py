class User:
    def __init__(self, login, password):
        self.login = login
        self.password = password


def login_attempt(user, login, password):
    if user.login == login and user.password == password:
        print("SUCCESS")
    else:
        print("WRONG CREDENTIONALS")
    
login_attempt(User(login="nika", password="nika"), "nika1", "nika")
