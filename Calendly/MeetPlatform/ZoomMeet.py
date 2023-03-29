from datetime import datetime
import  random

class ZoomMeet:
    def ZoomMeetLink(self):
        time = datetime.now()
        link = "Zoom" + str(random.random()) + str(time)
        return link
