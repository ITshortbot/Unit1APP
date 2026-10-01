# Library System - Mini Project
# Name: (add your name)
# This program uses classes to make a small library system

class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.borrowed = False

    def borrow(self):
        if self.borrowed:
            print(self.title, "is already taken.")
        else:
            self.borrowed = True
            print("You borrowed", self.title)

    def give_back(self):
        if self.borrowed:
            self.borrowed = False
            print(self.title, "returned. Thanks!")
        else:
            print(self.title, "wasn't borrowed anyway.")

    def show(self):
        status = "Borrowed" if self.borrowed else "Available"
        print(self.title, "-", self.author, "-", status)


class Patron:
    def __init__(self, name):
        self.name = name
        self.my_books = []

    def borrow_book(self, book):
        if book.borrowed:
            print("Can't borrow, someone else has it.")
        else:
            book.borrow()
            self.my_books.append(book)

    def return_book(self, book):
        if book in self.my_books:
            book.give_back()
            self.my_books.remove(book)
        else:
            print(self.name, "doesn't have that book.")


class Library:
    def __init__(self):
        self.books = []
        self.patrons = []

    def add_book(self, book):
        self.books.append(book)

    def add_patron(self, patron):
        self.patrons.append(patron)

    def find_book(self, isbn):
        for b in self.books:
            if b.isbn == isbn:
                return b
        print("No book with that isbn")
        return None

    def show_all_books(self):
        print("\n-- Books --")
        for b in self.books:
            b.show()


# ---- run the program ----

lib = Library()

b1 = Book("The Great Gatsby", "F. Scott Fitzgerald", "111")
b2 = Book("1984", "George Orwell", "222")
b3 = Book("To Kill a Mockingbird", "Harper Lee", "333")

lib.add_book(b1)
lib.add_book(b2)
lib.add_book(b3)

alice = Patron("Alice")
bob = Patron("Bob")
lib.add_patron(alice)
lib.add_patron(bob)

lib.show_all_books()

print("\n-- Borrowing --")
alice.borrow_book(b1)
bob.borrow_book(b1)     # should fail, already borrowed
bob.borrow_book(b2)

lib.show_all_books()

print("\n-- Returning --")
alice.return_book(b1)
bob.return_book(b1)     # bob never had it

lib.show_all_books()
