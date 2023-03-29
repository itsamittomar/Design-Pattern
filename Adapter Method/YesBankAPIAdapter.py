from BankPlatForm.YesBankAPI import YesBankAPI
from BankAdapter import BankInterface


class YesBankApiAdapter(BankInterface):
    def __init__(self):
        self.BankObject = YesBankAPI()
        



    def checkBalance(self):
        return self.BankObject.checkBalance()

    def authenticate(self):
        return self.BankObject.authenticateUser()

    def transaction(self):
        return self.BankObject.transaction()
    


