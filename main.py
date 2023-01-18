class Book:
    """ Базовый класс книги. """
    def __init__(self, name: str, author: str):
        self._name = name
        self._author = author

    """@property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if isinstance(name, str):
            self.__name = name
        else:
            raise TypeError

    @property
    def author(self):
        return self.__author

    @author.setter
    def author(self, author):
        if isinstance(author, str):
            self.__author = author
        else:
            raise TypeError"""

    def __str__(self):
        return f"Книга {self._name}. Автор {self._author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self._name!r}, author={self._author!r})"


class PaperBook(Book):
    def __init__(self, name, author, pages: None):
        super().__init__(name, author)
        self._pages = None
        self.init_pages(pages)

    def init_pages(self, pages: int):
        if not isinstance(pages, int):
            raise TypeError
        if pages < 0:
            raise ValueError
        self._pages = pages

    @property
    def pages(self):
        return self._pages

    @pages.setter
    def pages(self, pages):
        if not isinstance(pages, int):
            raise TypeError
        if pages < 0.0:
            raise ValueError
        self._pages = pages

    def __str__(self):
        return f"Книга {self._name}. Автор {self._author}. Страницы {self._pages}"
 

class AudioBook(Book):
    def __init__(self, name, author, duration: None):
        super().__init__(name, author)
        self._duration = None
        self.init_duration(duration)

    def init_duration(self, duration: float):
        if not isinstance(duration, float):
            raise TypeError
        if duration < 0:
            raise ValueError
        self._duration = duration

    @property
    def duration(self):
        return self._duration

    @duration.setter
    def duration(self, duration):
        if not isinstance(duration, float):
            raise TypeError
        if duration < 0:
            raise ValueError
        self._duration = duration

    def __str__(self):
        return f"Книга {self._name}. Автор {self._author}. Продолжительность {self._duration}"


if __name__ == "__main__":
    a = AudioBook('A', 'B', 10.1)
    print(a)
    a.author = 'F'
    #a.duration = 15.1
    print(a)

    a = PaperBook('A', 'B', 10)
    print(a)
    a. name = 'C'
    #a.pages = 100.5
    print(a)

    a = Book('A', 'B')
    print(a)
    a.name = 'F'
    a.author = 'C'
    print(a)









