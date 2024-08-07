class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self) -> str:
        pass


class EBook(Book):
    def __init__(self, title, author, file_size):
        super().__init__(title, author)
        self.file_size = file_size


class PrintBook(Book):
    def __init__(self, title, author, page_count):
        super().__init__(title, author)
        self.page_count = page_count


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def list_books(self):
        for b in self.books:

            if isinstance(b, EBook):
                print(f"EBook: {b.title} by {b.author}, File Size: {b.file_size}KB")
            elif isinstance(b, PrintBook):
                print(f"PrintBook: {b.title} by {b.author}, Page Count: {b.page_count}")
            elif isinstance(b, Book):
                print(f"Book: {b.title} by {b.author}")
