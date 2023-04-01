from PathCalculatorStrategy import PathCalculator
import threading


class BikePathCalculator(PathCalculator):
    __instance = None

    @staticmethod
    def getInstance():
        if BikePathCalculator.__instance is None:
            with threading.Lock():
                if BikePathCalculator.__instance is None:
                    BikePathCalculator.__instance == BikePathCalculator()

        return BikePathCalculator.__instance

    def findPath(self):
        print("Path calculator for Bike")
