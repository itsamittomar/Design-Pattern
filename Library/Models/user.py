import threading
class User:
    __userDetail = {}
    __instance= None

    def __init__(self):
        self.id = ""
        self.name = ""

    @staticmethod
    def getInstance():
        if User.__instance is None:
            with threading.Lock():
                if User.__instance is None:
                    User.__instance = User()
        return User.__instance


    @property
    def getId(self):
        return self.id

    @getId.setter
    def getId(self, userid):
        self.id = userid

    @property
    def getName(self):
        return self.name

    @getName.setter
    def getName(self, username):
        self.name = username

    def getUserDetail(self):
        return self.__userDetail
