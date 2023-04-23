from Library.Service.library import Library
class AvailableBooks:
    @staticmethod
    def prints():
        lib = Library.getInstance()
        dic = lib.getBook()
        for book, ids in dic.items():
            print(book, dic[book], end="\n")
