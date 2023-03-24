from singleton import SingletonInMultiThreading

def main():
    instance1 = SingletonInMultiThreading.getInstance()
    instance2= SingletonInMultiThreading.getInstance()
    instance3 = SingletonInMultiThreading.getInstance()

    print(instance1)
    print(instance2)
    print(instance3) 

if __name__ == '__main__':
    main()




