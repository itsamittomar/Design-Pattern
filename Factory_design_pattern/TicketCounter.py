from TicketTypes.DecideType import DecideType

class TicketCounter():
    def __init__(self) -> None:
        self.typ = None
        self.name = None
        self.sett = {'Premium', 'Economy', 'Business'}
        

    def getticketype(self):
        count = 3
        while count:
            self.typ = input('please inter ticket type you want to purchase: ')
            if self.typ not in self.sett:
                print('Invalid Ticket type entered, please enter valid type: Premium, Economy, Business')
                count -= 1
            else:
                break

    def getname(self):
        self.name = input('Please enter your full name: ')

    def createticketobject(self):
        return DecideType.decidetype(self.typ)

    