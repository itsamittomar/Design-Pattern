from NotificationService.Model.user import User
from NotificationService.Services.DecideUser import DecideUser
class NotificationController:

    def NotifyService(self, user_type):
        return DecideUser.decideUser(user_type)

