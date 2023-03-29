from MeetAdapter import MeetInterface
from Calendly.MeetPlatform.googleMeet import GoogleMeet

class GoogleMeetAdapter(MeetInterface):
    def __init__(self):
        self.MeetObject = GoogleMeet()

    def MeetLink(self):
        return self.MeetObject.GoogleMeetLink()
