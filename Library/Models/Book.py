from typing import Type

import threading
class Book:
    __instance = None
    __bookDetail = {}

    def __init__(self):
        self.__BookId = ""
        self.__title = ""
        self.__author = ""
        self.__publisher = ""
        self.__uniqueId = ""

    @staticmethod
    def getInstance():
        if Book.__instance is None:
            with threading.Lock():
                if Book.__instance is None:
                    Book.__instance = Book()

        return Book.__instance

    @property
    def bookId(self):
        return self.__BookId

    @bookId.setter
    def bookId(self, bookID):
        self.__BookId = bookID

    @property
    def bookTitle(self):
        return self.__title

    @bookTitle.setter
    def bookTitle(self, title):
        self.__title = title

    @property
    def bookAuthor(self):
        return self.__author

    @bookAuthor.setter
    def bookAuthor(self, authorName):
        self.__author = authorName

    @property
    def bookPublisher(self):
        return self.__publisher

    @bookPublisher.setter
    def bookPublisher(self, publisher):
        self.__publisher = publisher

    @property
    def bookUniqueId(self):
        return self.__uniqueId

    @bookUniqueId.setter
    def bookUniqueId(self, unique_id):
        self.__uniqueId = unique_id

    def getBookList(self):
        return self.__bookDetail

    def save(self):
        if self.__BookId not in self.__bookDetail:
            self.__bookDetail[self.__title] = [self.__BookId, self.__author, self.__publisher,self.__uniqueId]
            return self.__bookDetail
        else:
            return self.__bookDetail[self.__title].append([self.__BookId, self.__author, self.__publisher,self.__uniqueId])
