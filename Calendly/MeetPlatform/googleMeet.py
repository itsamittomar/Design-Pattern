from datetime import datetime
import  random
class GoogleMeet:

    def GoogleMeetLink(self):
        time = datetime.now()
        link= "Google" + str(random.random()) + str(time)
        return link