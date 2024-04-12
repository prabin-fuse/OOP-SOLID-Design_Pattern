class Book:

    def __init__(self,title, author, isbn, genre, availability):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.genre = genre
        self.availability = availability


class LibraryCatalog:

    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def get_book_details(self, title):
        for book in self.books:
            if title == book.title:
                return book

    def get_all_books(self):
        pass


class BorrowBook:

    def __init__(self):
        pass

    def valid_and_available(self, title):
        catalog = LibraryCatalog()
        book = catalog.get_book_details(title)
        if(book):
            return book
        
    def borrow_book(self, title):
        book = self.valid_and_available(title)
        if(book and book.availability):
            book.availablity = False
            print("The book is successfully borrowed.")
        elif(book and not book.availability):
            print("The book is not currently available.")
        else:
            print("The requested book is not availabe in the Library catalog")
