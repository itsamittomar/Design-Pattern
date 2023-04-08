from Amazon import Amazon
from CustomerNotifier import CustomerNotifier


def main():
    a = Amazon.getInstance()
    customer = CustomerNotifier()
    a.orderPlaced()
    a.orderCancelled()


if __name__ == '__main__':
    print(main())
