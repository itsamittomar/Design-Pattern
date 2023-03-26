class register:
    def __init__(self):
        self.registerDictionary = {}

    def get(self, train_name):
        return self.registerDictionary.get(train_name)

    def save(self, TrainObject):
        self.registerDictionary[TrainObject.getName()] = TrainObject
        print(self.registerDictionary)
