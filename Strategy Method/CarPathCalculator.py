from PathCalculatorStrategy import PathCalculator
import threading


class CarPathCalculator(PathCalculator):
    __instance = None

    def __init__(self):
        if CarPathCalculator.__instance is not None:
            raise Exception("Singleton class - Use getInstance() method to get the instance.")
        else:
            CarPathCalculator.__instance = self

    @staticmethod
    def getInstance():
        if CarPathCalculator.__instance is None:
            with threading.Lock():
                if CarPathCalculator.__instance is None:
                    CarPathCalculator.__instance = CarPathCalculator()

        return CarPathCalculator.__instance

    def findPath(self):
        print("Path Calculator for Car")
