from NotificationService.Model.user import User
from NotificationService.Controller.notificationController import NotificationController

if __name__ == '__main__':
    user = User()
    notification = NotificationController()
    user.setName("Amit Singh")
    user.setRole("Employee")
    userObject = notification.NotifyService(user.getRole())
    userObject.sendNotification()

