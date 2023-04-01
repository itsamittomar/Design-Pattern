from Map import Map
if __name__ == '__main__':
    MapObject = Map()
    MapObject.getSourceName()
    MapObject.getDestinationName()
    MapObject.getMode()
    mode = MapObject.getModeObject()
    mode.findPath()


