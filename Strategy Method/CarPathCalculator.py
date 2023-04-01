from PathCalculatorStrategy import PathCalculator
import threading
class CarPathCalculator(PathCalculator):
    __instance = None

    @staticmethod
    def getInstance():
        if CarPathCalculator.__instance is None:
            with threading.Lock():
                if CarPathCalculator.__instance is None:
                    CarPathCalculator.__instance = CarPathCalculator()

        return CarPathCalculator.__instance

    def findPath(self):
        print("Path Calculator for Car")


