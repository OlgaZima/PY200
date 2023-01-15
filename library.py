from typing import Iterable

BOOKS_DATABASE = [
    {
        "id": 1,
        "name": "test_name_1",
        "pages": 200,
    },
    {
        "id": 2,
        "name": "test_name_2",
        "pages": 400,
    }
]


# TODO написать класс Book
class Book:
    def __init__(self, id: int, name: str, pages: int):
        self.id = id
        self.name = name
        self.pages = pages

    def __str__(self) -> str:
        return f'id = {self.id}, {self.name}, {self.pages}'

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(id = {self.id}, name='{self.name}', pages={self.pages})"

# TODO написать класс Library


class Library:
    def __init__(self, books: Iterable = None):
        if books is None:
            books = []
        self.books = books

    def get_next_book_id(self):
        if isinstance(self.books, type(None)):
            return 1
        else:
            return len(self.books) + 1

    def __repr__(self) -> str:
        return f"({self.books})"

    def get_index_by_book_id(self, num: int):
        if self.books:
            res = 0
            for i in self.books:
                if i.id == num:
                    res = 1
                    return i.id - 1
            if res == 0:
                raise ValueError("Книги с запрашиваемым id не существует")


if __name__ == '__main__':
    empty_library = Library()  # инициализируем пустую библиотеку
    print(empty_library.get_next_book_id())  # проверяем следующий id для пустой библиотеки
    list_books = [
        Book(id=book_dict["id"], name=book_dict["name"], pages=book_dict["pages"]) for book_dict in BOOKS_DATABASE
    ]
    library_with_books = Library(books=list_books)  # инициализируем библиотеку с книгами
    print(library_with_books.get_next_book_id())  # проверяем следующий id для непустой библиотеки
    print(library_with_books.get_index_by_book_id(1))  # проверяем индекс книги с id = 1
