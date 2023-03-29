from MeetAdapter import MeetInterface
from Calendly.MeetPlatform.TeamMeet import TeamMeet

class TeamMeetAdapter(MeetInterface):
    def __init__(self):
        self.MeetObject = TeamMeet()

    def MeetLink(self):
        return self.MeetObject.TeamMeetLink()
