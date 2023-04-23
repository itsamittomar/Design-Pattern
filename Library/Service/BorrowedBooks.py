from Library.Service.library import Library
from Library.Models.Book import Book
import threading


class BorrowedBooks:
    __instance = None
    lib = Library.getInstance()
    book = Book()

    def __init__(self):
        self.bookname = ""
        self.userId = ""

    @staticmethod
    def getInstance():
        if BorrowedBooks.__instance is None:
            with threading.Lock():
                if BorrowedBooks.__instance is None:
                    BorrowedBooks.__instance = BorrowedBooks()

        return BorrowedBooks.__instance

    def borrowBook(self, bookname, userId):
        dic = self.lib.getBook()
        borrowed = self.lib.getBorrowedBooks()
        if bookname in dic:
            dic[bookname] -= 1
            borrowed[bookname].append(userId)
            print(borrowed, dic)

    def returnBook(self):
        dic = self.lib.getBook()
        borrowed = self.lib.getBorrowedBooks()
        if self.bookname in borrowed:
            dic[self.bookname] += 1
            borrowed[self.bookname] -= 1
        else:
            print("Invalid return !!!")
