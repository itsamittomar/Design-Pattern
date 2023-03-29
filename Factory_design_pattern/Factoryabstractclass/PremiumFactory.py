from Factoryabstractclass.TicketFactory import TicketFactory
from components.drinkmenu.PremiumDrink import PremiumDrink
from components.foodmenu.PremiumFood import PremiumFood
from components.seattype.PremiumSeat import PremiumSeat

class PremiumFactory(TicketFactory):

    def createdrink(self):
        return PremiumDrink()

    def createfood(self):
        return PremiumFood()

    def createseat(self):
        return PremiumSeat()