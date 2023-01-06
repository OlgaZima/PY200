# TODO Написать 3 класса с документацией и аннотацией типов
import doctest


class Players:
    def __init__(self, name: str, sex: str, age: int):
        """
        Создание и подготовка к работе объекта "Игроки"

        :param name: Имя игрока
        :param sex: Пол игрока
        :param age: Возраст игрока (полных лет)

        Примеры:
        >>> user = Players("Max", "man", 35,) # иницилизация экземпляра класса
        """
        if len(name) < 2:
            raise ValueError("Игрок должен иметь имя как min из 2-х букв")
        self.name = name

        if sex not in ("man", "woman"):
            raise ValueError("Пол игрока -  man or woman")
        self.sex = sex

        if not isinstance(age, int):
            raise TypeError("Возраст должен быть типа int")
        if age < 0:
            raise ValueError("Возраст должен быть положительным числом")
        self.age = age

        self.game = False

    def __str__(self) -> str:
        """
        Встроенная фун-ция для удобного представлния объекта пользователю

        :return: Описание игрока - имя, пол, возраст
        """
        return f"{self.name} - {self.sex}, {self.age} years"

    def start_game(self) -> str:
        """
        Фун-ция, описывающая состояние игрока на момент начала игры

        :return: Состояние игрока -в игре/уже в игре

        Примеры:
        >>> user = Players("Ann", "woman", 30)
        >>> user.start_game()
        'Ann в игре'
        >>> user.start_game()
        'Ann уже играет'
        >>> user.stop_game()
        'Ann вышел из игры'
        """
        if not self.game:
            self.game = True
            return f"{self.name} в игре"
        return f"{self.name} уже играет"

    def stop_game(self):
        """
        Фун-ция, описывающая состояние игрока на момент окончания игры

        :return: Состояние игрока - вышел из игры/уже вышел из игры

        Примеры:
        >>> user = Players("Mark", "man", 12)
        >>> user.stop_game()
        'Mark уже вышел из игры'
        """
        if self.game:
            self.game = False
            return f"{self.name} вышел из игры"
        return f"{self.name} уже вышел из игры"


if __name__ == "__main__":
    doctest.testmod()

    # TODO работоспособность экземпляров класса проверить с помощью doctest

