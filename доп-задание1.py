class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def __repr__(self):
        return f"Book({self.title}, {self.author}, {self.year})"


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def remove_book(self, book):
        self.books.remove(book)

    def find_book(self, author=None, title=None, year=None):
        if author:
            return [book for book in self.books if book.author == author]
        elif title:
            return [book for book in self.books if book.title == title]
        elif year:
            return [book for book in self.books if book.year == year]
        else:
            return self.books

    def sort_books(self, field, reverse=False):
        self.books.sort(key=lambda x: getattr(x, field), reverse=reverse)

    def __repr__(self):
        return f"Library({self.books})"


# Примеры использования
library = Library()

book1 = Book("Война и мир", "Лев Толстой", 1869)
book2 = Book("Преступление и наказание", "Федор Достоевский", 1866)
book3 = Book("Отцы и дети", "Иван Тургенев", 1862)

library.add_book(book1)
library.add_book(book2)
library.add_book(book3)

print(library.find_book(author="Лев Толстой"))

library.sort_books("year")
print(library)

library.remove_book(book2)
print(library)