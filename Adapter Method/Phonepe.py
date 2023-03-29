from BankAdapter import BankInterface
from YesBankAPIAdapter import YesBankApiAdapter
class PhonePe:
    def __init__(self):
        self.BankName = YesBankApiAdapter()

    def TransferMoney(self):
        print("inside ", self.BankName)
        if self.BankName.YesUserCheck():
            if self.BankName.YesUserCheck():
                if self.BankName.YesTransactionCheck():
                    print(f'Transaction Completed')



if __name__ == '__main__':
    call = PhonePe()
    call.TransferMoney()
