from BankPlatForm.YesBankAPI import YesBankAPI
from BankAdapter import BankInterface


class YesBankApiAdapter(BankInterface):
    def __int__(self):
        self.BankObject = YesBankAPI



    def YesCheckBalance(self):
        return self.BankObject.queryBalance()

    def YesUserCheck(self):
        print(self.BankObject,"Bank Object")
        return self.BankObject.checkUser()

    def YesTransactionCheck(self):
        return self.BankObject.checkTransaction()
