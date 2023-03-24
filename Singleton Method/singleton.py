import threading

class SingletonInMultiThreading:
    __instance = None

    @staticmethod
    def getInstance():
        if SingletonInMultiThreading.__instance == None:
            with threading.Lock():
                if SingletonInMultiThreading.__instance == None:
                    SingletonInMultiThreading.__instance = SingletonInMultiThreading()
            

        return SingletonInMultiThreading.__instance

   
