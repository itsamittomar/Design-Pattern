from Amazon import Amazon
from CustomerNotifier import CustomerNotifier

def main():
    a = Amazon.getInstance()
    customer = CustomerNotifier()
    a.orderPlaced()



if __name__ == '__main__':
    main()







