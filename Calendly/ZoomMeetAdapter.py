from MeetAdapter import MeetInterface
from Calendly.MeetPlatform.ZoomMeet import ZoomMeet

class ZoomMeetAdapter(MeetInterface):
    def __init__(self):
        self.MeetObject = ZoomMeet()

    def MeetLink(self):
        return self.MeetObject.ZoomMeetLink()

