from Train import LocalTrain , Train
import datetime

def main():
    localTrain = Train()
    localTrain.setfare(250)
    localTrain.settrain_type("EMU")
    localTrain.setengine_type("Electric")
    localTrain.setno_of_seats(50)
    
    
    ExpressTrain = localTrain.clone()
    ExpressTrain.settiming("1:00 PM")
    ExpressTrain.setsource_station("NZM")
    ExpressTrain.setdestination_station("KNP")
    print(ExpressTrain)

    FastTrain = localTrain.clone()
    FastTrain.settiming("3:00 PM")
    FastTrain.setsource_station("KNP")
    FastTrain.setdestination_station("NZM")
    print(FastTrain)




if __name__ =="__main__":
    main()