# TODO Написать 3 класса с документацией и аннотацией типов
from typing import Union
import doctest


class Rectangle:
    def __init__(self, x1, x2, y1, y2: Union[int, float]):
        """
        Создание и подготовка к работе объета "Прямоугольник"

        :param x1: координата x в декартовой с-ме координат
        :param x2: "-"
        :param y1: координата y в декартовой с-ме координат
        :param y2: "-"
        Примеры:
        #>>> rec = Rectangle(-1, 0.0, -1, 0.0)
        """
        if not isinstance(x1, (int, float)) or not isinstance(x2, (int, float)) or not isinstance(y1, (int, float)) or not isinstance(y2, (int, float)):
            raise TypeError("Неправильный тип")
        if x1 == x2 and y1 == y2:
            raise ValueError("Это не прямоугольник")
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2

    def wid_len(self, a1, a2) -> float:
        """
        Фун-ция, рассчитывающая ширину/длину прямоугольника, заданного в декартовой с-ме координат

        :param a1: координаты x1/y1
        :param a2: координаты x2/y2
        :return: Ширину/Длину
        Примеры:
        >>> rec = Rectangle(0, 10, 1, 0)
        >>> rec.wid_len(0, 10)
        10
         >>> rec.wid_len(-5, -6)
         1
         >>> rec.wid_len(5, -6)
         11
        """
        if (a1 and a2) < 0:
            if a1 < a2:
                widlen = a2 - a1
            else:
                widlen = a1 - a2
        elif (a1 and a2) >= 0:
            if a1 < a2:
                widlen = a2 - a1
            else:
                widlen = a1 - a2
        elif a1 < 0 and a2 >= 0:
            widlen = a2 - a1
        else:
            widlen = a1 - a2
        return widlen

    def area(self) -> Union[int, float]:
        """
        Фун-ция, рассчитывающая S прямоугольника

        :return: S прямоугольника
        Примеры:
        >>> rec1 = Rectangle(-1, 2, 0, -2)
        >>> rec1.area()
        6
        """
        rec = Rectangle(1, 0, 1, 0)
        area_ = rec.wid_len(self.x1, self.x2) * rec.wid_len(self.y1, self.y2)
        return area_

    def perimetr(self) -> Union[int, float]:
        """
        Фун-ция, рассчитывающая периметр прямоугольника

        :return: Периметр прямоугольника
        Примеры:
        >>> rec2 = Rectangle(-1, 2, -1, 3)
        >>> rec2.perimetr()
        14
        """
        rec = Rectangle(-5, 0, -3, 3)
        perimetr_ = 2 * (rec.wid_len(self.y1, self.y2) + rec.wid_len(self.x1, self.x2))
        return perimetr_


if __name__ == "__main__":
    doctest.testmod()

