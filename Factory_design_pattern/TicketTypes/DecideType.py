from TicketTypes.TicketsTypes import TicketTypes
from Factoryabstractclass.BusinessFactory import BusinessFactory
from Factoryabstractclass.EconomyFactory import EconomyFactory
from Factoryabstractclass.PremiumFactory import PremiumFactory

class DecideType:

    @staticmethod
    def decidetype(typ):
        if typ == TicketTypes.Premium.name:
            return PremiumFactory()
        elif typ == TicketTypes.Business.name:
            return BusinessFactory()
        elif typ == TicketTypes.Economy.name:
            return EconomyFactory()
        else:
            raise Exception (f'Invalid Ticket type: "{typ}')