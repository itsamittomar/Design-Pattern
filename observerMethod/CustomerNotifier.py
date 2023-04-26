from OrderedPlacedSubscriber import OrderPlacedSubscriber
from OrderedCancelledSubsriber import OrderCancelledSubscriber
from Amazon import Amazon


class CustomerNotifier(OrderCancelledSubscriber, OrderPlacedSubscriber):

    def __init__(self):
        Object = Amazon()
        Object.registerSubscriber(self)
        Object.registerOrderCancelledSubscriber(self)

    def orderPlaced(self):
        print("Notify all the Customers")

    def orderCancelled(self):
        print("Notify customer for the cancellation")
