import random

from Library.Models.user import User
from Library.Models.Rack import Rack
from Library.Service.library import Library
from Library.Service.BorrowedBooks import BorrowedBooks
from Library.Service.BookDetails import BookDetails
from Library.Service.AvailableBookInLibrary import AvailableBooks
import Library.Service.AddBookDetails as add
from Library.Models.user import User


def client():
    add.AddBook()
    lib = Library.getInstance()
    dic = lib.getBook()
    print("Available Books in the Library")
    AvailableBooks.prints()
    name = input("Enter book name to borrow: ")
    username = input("Enter your name: ")
    userId = random.randrange(1, 1000)
    userDic = User.getInstance().getUserDetail()
    borrow = BorrowedBooks.getInstance()
    if username not in userDic:
        userDic[userId] = username
        borrow.borrowBook(name, userId)
    else:
        borrow.borrowBook(name, userId)
    print(userDic)
    print(dic)


if __name__ == '__main__':
    client()
