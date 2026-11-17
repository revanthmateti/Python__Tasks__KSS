class Book:

    def __init__(self, title, author):
        self.title = title
        self.author = author


class EBook(Book):

    def __init__(self, title, author, filesize):
        super().__init__(title, author)
        self.filesize = filesize

    def display(self):
        print("Book Title:", self.title)
        print("Author:", self.author)
        print("File Size:", self.filesize)


e1 = EBook("Python Programming", "John", "5MB")

e1.display()
