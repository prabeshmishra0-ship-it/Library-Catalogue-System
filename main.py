
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.available = True

    def display_info(self):
        print("Title:", self.title)
        print("Author:", self.author)
        if self.available:
            print("Status: Available")
        else:
            print("Status: Checked out")

    def check_out(self):
        if self.available:
            self.available = False
            print(self.title, "has been checked out.")
        else:
            print(self.title, "is already checked out.")

    def return_book(self):
        if not self.available:
            self.available = True
            print(self.title, "has been returned.")
        else:
            print(self.title, "is already available.")


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        print(book.title, "added to the library.")

    def display_books(self):
        if not self.books:
            print("No books in the library.")
        else:
            print("\n--- Library Catalogue ---")
            for book in self.books:
                print()
                book.display_info()


def main():
    library = Library()

    book1 = Book("Harry Potter", "J.K. Rowling")
    book2 = Book("The Hobbit", "J.R.R. Tolkien")

    library.add_book(book1)
    library.add_book(book2)

    library.display_books()

    print("\n--- Checking Out a Book ---")
    book1.check_out()

    print("\n--- Updated Catalogue ---")
    library.display_books()

    print("\n--- Returning a Book ---")
    book1.return_book()

    print("\n--- Final Catalogue ---")
    library.display_books()

    return


if __name__ == "__main__":
    main()
