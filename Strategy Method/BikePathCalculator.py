from PathCalculatorStrategy import PathCalculator
import threading


class BikePathCalculator(PathCalculator):
    __instance = None

    def __init__(self):
        if BikePathCalculator.__instance is not None:
            raise Exception("Singleton class - Use getInstance() method to get the instance.")
        else:
            BikePathCalculator.__instance = self

    @staticmethod
    def getInstance():
        if BikePathCalculator.__instance is None:
            with threading.Lock():
                if BikePathCalculator.__instance is None:
                    BikePathCalculator.__instance == BikePathCalculator()

        return BikePathCalculator.__instance

    def findPath(self):
        print("Path calculator for Bike")
