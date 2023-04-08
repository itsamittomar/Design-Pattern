import threading


class Amazon:
    __instance = None
    _orderCancelledSubscriber = {}
    _orderPlacedSubscriber = {}

    @staticmethod
    def getInstance():
        if Amazon.__instance is None:
            with threading.Lock():
                if Amazon.__instance is None:
                    Amazon.__instance = Amazon()

        return Amazon.__instance

    def registerSubscriber(self, subscriber):
        if subscriber in self._orderPlacedSubscriber:
            print(self._orderPlacedSubscriber)
            pass
        else:
            self._orderPlacedSubscriber[subscriber] = 1

    def deregisterSubscriber(self, subscriber):
        if subscriber in self._orderPlacedSubscriber:
            del self._orderPlacedSubscriber[subscriber]
        else:
            print(subscriber, "is not your subscriber")

    def registerOrderCancelledSubscriber(self, subscriber):
        if subscriber in self._orderCancelledSubscriber:
            pass
        else:
            self._orderCancelledSubscriber[subscriber] = 1

    def deregisterOrderCancelledSubscriber(self, subscriber):
        if subscriber in self._orderCancelledSubscriber:
            del self._orderCancelledSubscriber[subscriber]
        else:
            print(subscriber, "has already unsubscribed from the notification service")

    def orderPlaced(self):
        for subscriberObject in self._orderPlacedSubscriber:
            subscriberObject.orderPlaced()

    def orderCancelled(self):
        for subscriberObject in self._orderCancelledSubscriber:
            subscriberObject.orderPlaced()
