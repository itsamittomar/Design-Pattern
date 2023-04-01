from ModeTypes import ModeType
from BikePathCalculator import BikePathCalculator
from CarPathCalculator import CarPathCalculator
from FlightPathCalculator import FlightPathCalculator

class DecideMode:

    @staticmethod
    def decideMode(typ):
        if typ == ModeType.Car.name:
            return CarPathCalculator()
        elif typ == ModeType.Bike.name:
            return BikePathCalculator()
        elif typ == ModeType.Flight.name:
            return FlightPathCalculator()
        else:
            raise Exception (f'Invalid Mode type: "{typ}')