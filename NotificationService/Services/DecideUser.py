from NotificationService.Model.DeliveryGuy import DeliveryGuy
from NotificationService.Model.Employee import Employee
from NotificationService.Model.EndUser import EndUser
from NotificationService.UserType import UserType


class DecideUser:

    @staticmethod
    def decideUser(typ):
        if typ == UserType.DeliveryGuy.name:
            return DeliveryGuy()
        elif typ == UserType.Employee.name:
            return Employee()
        elif typ == UserType.EndUser.name:
            return EndUser()
        else:
            raise Exception (f'Invalid Mode type: "{typ}')