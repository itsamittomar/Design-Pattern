import copy 
from prototype import prototype

class LocalTrain :
    def __init__(self):
        self.name=""
        self.fare =0
        self.train_type =""
        self.engine_type=""
        self.no_of_seats =0
        self.timing =""
        self.source_station =""
        self.destination_station = ""
    

class Train(LocalTrain , prototype):

    def __init__(self):
        super().__init__()
       
        self.Tainfare = self.fare
        self.train_type = self.train_type
        self.engine_type =self.engine_type
        self.no_of_seats = self.no_of_seats 
        
    

    def clone(self):
        return copy.deepcopy(self)
    

    def getfare(self):
        return self.fare
    

    def setfare(self,fare):
        self.fare = fare 
    

    def gettrain_type(self):
        return self.train_type
    

    def settrain_type(self,vlaue):
        self.train_type = vlaue
    

    def getengine_type(self):
        return self.engine_type
    

    def setengine_type(self,vlaue):
        self.engine_type = vlaue


    def getno_of_seats(self):
        return self.no_of_seats
    

    def setno_of_seats(self,val):
        self.no_of_seats = val
    

    def gettiming(self):
        return self.timing
    

    def settiming(self,val):
        self.timing = val 

 
    def getsource_station(self):
        return self.source_station
    

    def setsource_station(self,val):
        self.source_station = val 
    

    def getdestination_station(self):
        return self.destination_station
    
   
    def setdestination_station(self,val):
        self.destination_station = val 
    

    def __str__(self) -> str:
        return "LocalTrain{"  + \
                "fare=" + str(self.fare) + \
                ", trainType='" + self.train_type + '\'' + \
                ", engineType='" + self.engine_type + '\'' + \
                ", noOfSeats=" + str(self.no_of_seats) + \
                ", timing='" + self.timing + '\'' + \
                ", destination station='" + self.destination_station + '\'' + \
                ", source station='" + self.source_station + '\'' + \
                '}'
    


    

    

