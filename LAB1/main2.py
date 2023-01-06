import doctest


abs_book = [["Python", "Matiz", 126], ["Python", "Matiz", 500]]     #Условный каталог книг


class Books:
    def __init__(self, title_: str, author: str, page: int):
        """
        Создание и подготовка к работе объекта "Книги"

        :param title_: Название книги
        :param author: Авторы
        :param page: Кол-во страниц

        Примеры:
        >>> book = Books("Python", "Matiz", 126)
        """
        if not isinstance(title_, str):
            raise TypeError("Название книги должно быть типа str")
        self.title_ = title_

        if not isinstance(author, str):
            raise TypeError("Авторы должны быть типа str")
        self.author = author

        if not isinstance(page, int):
            raise TypeError("Кол-во страниц должно быть типа int")
        if page < 0:
            raise ValueError("Кол-во страниц должно быть положительным числом")
        self.page = page

        self.last_page = 0

    def check_book(self) -> str:
        """
        Фун-ция, которая проверяет есть ли книга в условном каталоге "abs_book"

        :return: Строка: есть/нет книг(а/и) в каталоге
        Примеры:
        >>> book = Books("Python", "Matiz", 126)
        >>> book.check_book()
        Книга есть в каталоге
        """
        book_ = [self.title_, self.author, self.page]
        for i in abs_book:
            if i == book_:
                return print("Книга есть в каталоге")
                break
            raise ValueError("Такой книги нет в каталоге")

    def read_page(self, page_read: int) -> None:
        """
        Фун-ция, увеличивающая кол-во прочитанных страниц

        :param page_read: Кол-во прочитанных страниц
        :return: None

        Примеры:
        >>> book = Books("Python", "Matiz", 126)
        >>> book.read_page(126)
        """
        if not isinstance(page_read, int):
            raise TypeError("Прочитанные страницы должны быть типа int")

        if page_read > self.page or page_read < 0:
            raise ValueError("Прочитанные стр. должны быть + числом и кол-во прочит. стр. < кол-во стр. в книге")
        self.last_page += page_read


if __name__ == "__main__":
    doctest.testmod()






