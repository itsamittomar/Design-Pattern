from ModeTypes import ModeType
from BikePathCalculator import BikePathCalculator
from CarPathCalculator import CarPathCalculator
from FlightPathCalculator import FlightPathCalculator
from WalkPathCalculator import WalkPathCalculator

class DecideMode:

    @staticmethod
    def decideMode(typ):
        if typ == ModeType.Car.name:
            return CarPathCalculator()
        elif typ == ModeType.Bike.name:
            return BikePathCalculator()
        elif typ == ModeType.Flight.name:
            return FlightPathCalculator()
        elif typ == ModeType.Walk.name:
            return WalkPathCalculator()
        else:
            raise Exception (f'Invalid Mode type: "{typ}')