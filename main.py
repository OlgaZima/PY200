class Book:
    """ Базовый класс книги. """
    def __init__(self, name: str, author: str):
        self._name = name
        self._author = author

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        raise ValueError("Только для чтения")

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, author):
        raise ValueError("Только для чтения")

    def __str__(self):
        return f"Книга {self._name}. Автор {self._author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self._name!r}, author={self._author!r})"


class PaperBook(Book):
    def __init__(self, name, author, pages: int):
        super().__init__(name, author)
        self.pages = pages

    @property
    def pages(self):
        return self._pages

    @pages.setter
    def pages(self, p):
        if not isinstance(p, int):
            raise TypeError("Должно быть целочисленным")
        if p < 0:
            raise ValueError("Должно быть положительным")
        self._pages = p

    def __str__(self):
        return f"Книга {self._name}. Автор {self._author}. Страницы {self._pages}"
 

class AudioBook(Book):
    def __init__(self, name, author, duration: None):
        super().__init__(name, author)
        self.duration = duration

    @property
    def duration(self):
        return self._duration

    @duration.setter
    def duration(self, d):
        if not isinstance(d, float):
            raise TypeError("Должно быть десятичным числом")
        if d < 0:
            raise ValueError("Должно быть положительным числом")
        self._duration = d

    def __str__(self):
        return f"Книга {self._name}. Автор {self._author}. Продолжительность {self._duration}"


if __name__ == "__main__":
    print('PaperBook______________________')
    a = PaperBook('Airport', 'Haley', 10)
    print(a)
    a.pages = 100
    print(a)
    print(a.author)
    #a = PaperBook('A', 'B',-10)
    #a.pages = - 10
    #a = PaperBook('A', 'B', 'C')
    #a.author = 'C'

    print('AudioBook______________________')
    b = AudioBook('Airport', 'Haley', 10.1)
    print(b)
    b.duration = 15.2
    print(a)
    print(b.name)
    #b.name = 'C'
    #b = AudioBook('A', 'B', '1234.5')
    #b.duration = -10

    print('Book______________________')
    b = Book('Airport', 'Haley')
    print(b)
    print(b.name)
    print(b.author)
    #b.name = 'C'

















