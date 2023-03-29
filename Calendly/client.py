
from GoogleMeetAdapter import GoogleMeetAdapter
from ZoomMeetAdapter import ZoomMeetAdapter
from TeamsMeetAdapter import TeamMeetAdapter

class Client:
    def __init__(self):
        self.MeetLinkObject = TeamMeetAdapter()


    def GetMeetLink(self):
        return self.MeetLinkObject.MeetLink()



if __name__ == '__main__':
    obj = Client()
    print(obj.GetMeetLink())

