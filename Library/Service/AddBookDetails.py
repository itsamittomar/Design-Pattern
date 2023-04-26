import random
import uuid
from Library.Models.Book import Book
from Library.Service.library import Library
def AddBook():

    print("How many books you want to add")
    number = int(input())
    for i in range(number):
        print("Enter title , Author,Publisher for the book ")
        num = input().split(",")
        book = Book.getInstance()
        book.bookId = random.random()
        book.bookTitle = num[0]
        book.bookAuthor = num[1]
        book.bookUniqueId = uuid.uuid4()
        book.bookPublisher = num[2]
        book.save()
        lib = Library.getInstance()
        lib.addBook(book.bookTitle)


