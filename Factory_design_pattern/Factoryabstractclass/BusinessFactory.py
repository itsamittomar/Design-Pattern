from Factoryabstractclass.TicketFactory import TicketFactory
from components.drinkmenu.BusinessDrink import BusinessDrink
from components.foodmenu.BusinessFood import BusinessFood
from components.seattype.BusinessSeat import BusinessSeat

class BusinessFactory(TicketFactory):

    def createdrink(self):
        return BusinessDrink()


    def createfood(self):
        return BusinessFood()

    def createseat(self):
        return BusinessSeat()