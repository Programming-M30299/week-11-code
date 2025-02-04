class Book:

    def __init__(self, title, author, isbn):
        # Create the instance variables for title, author, and isbn here
        self.available = True  # Initially, the book is available

    def borrow_book(self):
        # Remove the pass and write code for this method
        # (borrowing a book changes its availability)
        pass

    def return_book(self):
        # Remove the pass and write code for this method
        pass

    def __str__(self):
        # Remove the pass and write code for this method
        #  (printing a book should display its title, author, and isbn)
        pass


class DigitalBook(Book):

    def __init__(self, title, author, isbn):
        # Call the superclass constructor with title, author, and isbn
        self.compatibility = {'Kindle'}

    def borrow_book(self):
        # Don't remove the pass
        # (borrowing a digital book doesn't change its availability)
        pass

    def return_book(self):
        # Don't remove the pass (same as borrow_book)
        pass

    def __str__(self):
        # Remove the pass and write code for this method
        # (printing a digital book should also display its compatibility)
        pass


class Library:

    def __init__(self):
        self.books = []

    def add_book(self, book):
        # Remove the pass and write code for this method
        pass

    def borrow_book(self, title):
        for book in self.books:
            if book.title == title:
                # Remove the pass and write code for this method
                # (check if the book is available, then call its borrow method)
                pass

    def return_book(self, title):
        # Remove the pass and write code for this method, see borrow_book
        pass

    def __str__(self):
        # Remove the pass and write code for this method
        # (printing a library should display its books and their details)
        pass


def test_book():
    book = Book('Frankenstein', 'Mary Shelley', '978-0486282114')
    # Try the methods of the Book class here and print the book object


def test_digital_book():
    digital_book = DigitalBook(
        'Orlando: A Biography', 'Virginia Woolf', '978-0156031516')
    # Try the methods here and print it


def test_library():
    Book("The Great Gatsby", "F. Scott Fitzgerald", "978-0743273565")
    Book("1984", "George Orwell", "978-0451524935")
    Book("Jane Eyre", "Charlotte Bronte", "978-0141441146")
    DigitalBook("1984", "George Orwell", "978-0451524935")

    library = Library()
    # Add the books to the library here and try borrowing and returning them
    # Remember to print the library object at each step
