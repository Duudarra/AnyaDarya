class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def get_info(self):
        return f"'{self.title}' by {self.author}, published in {self.year}"


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def list_books(self):
        if not self.books:
            return "No books in the library."
        return "\n".join([book.get_info() for book in self.books])


if __name__ == "__main__":
    book1 = Book("1984", "Джордж Оруэлл", 1949)
    book2 = Book("Война и мир", "Лев Толстой", 1863)

    library = Library()

    library.add_book(book1)
    library.add_book(book2)

    print("Books in the library:")
    print(library.list_books())
    