class Book:
    def __init__(self, name: str, author: str, pages: int):
        self._name = name
        self._author = author
        self._pages = pages

    @property
    def name(self):
        return self._name

    @property
    def author(self):
        return self._author

    @property
    def pages(self):
        return self._pages


class Library(Book):
    book_count = 0

    def __init__(self, name: str, author: str, pages: int, year: None):
        super().__init__(name, author, pages)
        self.year = year
        self.add_book_count()

    @property
    def year(self):
        return self._year

    @year.setter
    def year(self, year_):
        if not isinstance(year_, int):
            raise TypeError()
        if year_ < 1900 or year_ > 2023:
            raise ValueError()
        self._year = year_

    @classmethod
    def add_book_count(cls):
        cls.book_count += 1

    @staticmethod
    def check_id(b1, b2):
        return b1.name == b2.name and b1.author == b2.author

    def __str__(self):
        return f"Название {self._name}. Автор {self._author}. Страницы {self._pages}. Год {self.year}"


if __name__ == "__main__":
    book1 = Library('Аэропорт', 'Хейли', 123, 1968)
    print(Library.book_count)
    book2 = Library('Аэропорт', 'Хейли', 123, 1968)
    print(Library.book_count)
    print(Library.book_count)
    print(Library.check_id(book1, book2))

    # Write your solution here
    #pass
