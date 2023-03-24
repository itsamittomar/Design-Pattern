from Train import LocalTrain , Train
from TrainRegistry import register
import datetime

def main():
    localTrain = Train()
    localTrain.setName("Local")
    localTrain.setfare(250)
    localTrain.settrain_type("EMU")
    localTrain.setengine_type("Electric")
    localTrain.setno_of_seats(50)
    
    Express = Train()
    Express.setName("Express Train")
    Express.setfare(200)
    Express.settrain_type("EMU Fast")
    Express.setengine_type("Electric ")
    Express.setno_of_seats(60)

    Fast = Train()
    Fast.setName("Fast Train")
    Fast.setfare(200)
    Fast.settrain_type("Fast Train")
    Fast.setengine_type("Coal ")
    Fast.setno_of_seats(55) 

    womenspecial = Train()
    womenspecial.setName("Women")
    womenspecial.setfare(100)
    womenspecial.settrain_type("Special")
    womenspecial.setengine_type("Electric ")
    womenspecial.setno_of_seats(55)

    register_instance = register()
    register_instance.save(Express)
    register_instance.save(Fast)
    register_instance.save(womenspecial)


    
    
    express = register_instance.get("Express Train")
    ExpressTrain = express.clone()
    ExpressTrain.settiming("1:00 PM")
    ExpressTrain.setsource_station("NZM")
    ExpressTrain.setdestination_station("KNP")
    print(ExpressTrain)

    fast = register_instance.get("Fast Train")
    FastTrain = fast.clone()
    FastTrain.settiming("3:00 PM")
    FastTrain.setsource_station("KNP")
    FastTrain.setdestination_station("NZM")
    print(FastTrain)


    women = register_instance.get("Women")
    womenspecial = women.clone()
    womenspecial.settiming("08:00 AM")
    womenspecial.setsource_station("DEL")
    womenspecial.setdestination_station("KNP")
    print(womenspecial)



if __name__ =="__main__":
    main()