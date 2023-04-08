from PathCalculatorStrategy import PathCalculator
import threading


class FlightPathCalculator(PathCalculator):
    __instance = None

    def __init__(self):
        if FlightPathCalculator.__instance is not None:
            raise Exception("Singleton class - Use getInstance() method to get the instance.")
        else:
            FlightPathCalculator.__instance = self

    @staticmethod
    def getInstance():
        if FlightPathCalculator.__instance is None:
            with threading.Lock():
                if FlightPathCalculator.__instance is None:
                    FlightPathCalculator.__instance == FlightPathCalculator()

        return FlightPathCalculator.__instance

    def findPath(self):
        print("Path calculator for flight")
