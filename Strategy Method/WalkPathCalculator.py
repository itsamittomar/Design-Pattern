import threading

from PathCalculatorStrategy import PathCalculator


class WalkPathCalculator(PathCalculator):
    __instance = None

    def __init__(self):
        if WalkPathCalculator.__instance is not None:
            raise Exception("Singleton class - Use getInstance() method to get the instance.")
        else:
            WalkPathCalculator.__instance = self

    @staticmethod
    def getInstance():
        if WalkPathCalculator.__instance is None:
            with threading.Lock():
                if WalkPathCalculator.__instance is None:
                    WalkPathCalculator.__instance = WalkPathCalculator

        return WalkPathCalculator.__instance

    def findPath(self):
        print("Path Calculator for Walking ")
