
class Book:

    def __init__(self, title, author, bookname, pages):
        self.title = title
        self.author = author
        self.bookname = bookname
        self.pages = pages

    def __str__(self):
        return "Title: %s, author: %s, pages: %s" % (self.title, self.author, self.bookname)

    def __len__(self):
        return self.pages

    def __eq__(self, other):
        return self.title == other

    def __bool__(self):
        return self.bookname == ""

    def __del__(self):
        print("delete a book")

    def __add__(self, other):
        return self.pages + other

    def __gt__(self, other):
        return self.pages > other

book = Book("Python Course", "ramin", "python for anywhere", 123)
print(book)
print(len(book))
print(book.__eq__("Python Course"))
print(book.__bool__())
print(book.__add__(10))
print(book.__gt__(300))
del book
