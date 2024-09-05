"""
method vs @classmethod vs @staticmethod
method - self, método de instância
@classmethod - cls, método da classe
@staticmethod - método estático (sem self, sem cls)
"""

class Connection:
    def __init__(self, host='localhost', user=None, password=None):
        self.host = host
        self.user = None
        self.password = None

    def set_user(self, user):
        self.user = user

    def get_user(self):
        return self.user
    
    def set_password(self, password):
        self.password = password

    def get_password(self):
        return self.password
    
    @classmethod
    def create_with_auth(cls, user, password):
        connection = cls()
        connection.set_user(user)
        connection.set_password(password)
        return connection
    
    @staticmethod
    def log(msg):
        print("LOG", msg)

# c1 = Connection()
# c1.set_user('root')
# c1.set_password('root')
# print(c1.user)
# print(c1.password)

c2 = Connection.create_with_auth('root', '87Ab@')
print(c2.user)
print(c2.password)
Connection.log("Essa é a mensagem de log")