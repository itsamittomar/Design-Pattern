from abc import ABC


class BankInterface(ABC):
    def checkBalance(self):
        pass

    def checkUser(self):
        pass

    def checkTransaction(self):
        pass
