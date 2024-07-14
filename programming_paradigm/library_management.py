class Book:
    def __init__(self, title, author, _is_checked_out=False):
        self.title = title
        self.author = author
        self._is_checked_out = _is_checked_out

    def check_out(self):
        if not self._is_checked_out:
            self._is_checked_out = True
            return True
        else:
            return False

    def return_book(self):
        if self._is_checked_out:
            self._is_checked_out = False
            return True
        else:
            return False


class Library:
    def __init__(self):
        _books = []
        self.book = _books

    def add_book(self, newBook):
        self.book.append(newBook)

    def list_available_books(self):
        for book in self.book:
            print(f"{book.title} by {book.author}")

    def check_out_book(self, title):
        for book in self.book:
            if book.title == title:
                return book.check_out()
        return False

    def return_book(self, title):
        for book in self.book:
            if book.title == title:
                return book.return_book()
            return False

