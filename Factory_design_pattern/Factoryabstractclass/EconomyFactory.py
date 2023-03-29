from Factoryabstractclass.TicketFactory import TicketFactory
from components.drinkmenu.EconomyDrink import EconomyDrink
from components.foodmenu.EconomyFood import EconomyFood
from components.seattype.EconomySeat import EconomySeat

class EconomyFactory(TicketFactory):

    def createdrink(self):
        return EconomyDrink()

    def createfood(self):
        return EconomyFood()

    def createseat(self):
        return EconomySeat()