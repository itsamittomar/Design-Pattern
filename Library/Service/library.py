from collections import defaultdict

import threading
class Library:
    __instance =None
    __books = {}
    __borrowedBooks = defaultdict(list)
    @staticmethod
    def getInstance():
        if Library.__instance is None:
            with threading.Lock():
                if Library.__instance is None:
                    Library.__instance = Library()

        return Library.__instance

    def addBook(self, bookName):
        if bookName not in self.__books:
            self.__books[bookName] = 1
        else:
            self.__books[bookName] += 1

    def remove(self, name):
        if name not in self.__books:
            return "Book Not Found!!!"
        if name in self.__books and self.__books[name] > 0:
            self.__books[name] -= 1
        else:
            del self.__books[name]

    def getBook(self):
        return self.__books

    def getBorrowedBooks(self):
        return self.__borrowedBooks


