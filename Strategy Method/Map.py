from DecideMode import DecideMode


class Map:
    def __init__(self):
        self.source = ""
        self.destination = ""
        self.mode = {"Bike", "Car", "Flight"}
        self.TravellingMode = ""

    def getSourceName(self):
        self.source = input("Enter Your source: ")

    def getDestinationName(self):
        self.destination = input("Enter Your destination: ")

    def getMode(self):
        mode = input("Enter Your Preferred Travelling mode: ")
        if mode not in self.mode:
            print("Please Enter the valid Mode!!!")
        else:
            self.TravellingMode = mode

    def getModeObject(self):
        return DecideMode.decideMode(self.TravellingMode)
