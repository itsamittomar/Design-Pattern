import threading


class SingletonInMultiThreading:
    __instance = None

    def __init__(self):
        if SingletonInMultiThreading.__instance is not None:
            raise Exception("Singleton class - Use getInstance() method to get the instance.")
        else:
            SingletonInMultiThreading.__instance = self

    @staticmethod
    def getInstance():
        if SingletonInMultiThreading.__instance is None:
            with threading.Lock():
                if SingletonInMultiThreading.__instance is None:
                    SingletonInMultiThreading.__instance = SingletonInMultiThreading()

        return SingletonInMultiThreading.__instance
