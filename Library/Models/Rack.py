class Rack:
    _booklist = {}

    def __init__(self, booklist):
        self.rackid = ""
        self._booklist = booklist

    @property
    def getrackId(self):
        return self.rackid

    @getrackId.setter
    def getrackId(self,rackID):
        self.rackid = rackID

    @property
    def getList(self):
        return self._booklist

    @getList.setter
    def getList(self,lis):
        self._booklist = lis
