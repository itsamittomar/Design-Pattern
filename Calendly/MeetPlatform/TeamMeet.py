from datetime import datetime
import  random

class TeamMeet:
    def TeamMeetLink(self):
        time = datetime.now()
        link = "Team" + str(random.random()) + str(time)
        return link
