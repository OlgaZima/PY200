class Date:
    """Класс для работы с датами"""
    DAY_OF_MONTH = (
        (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31),  # обычный год
        (31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)  # високосный
    )

    def __init__(self, day: int, month: int, year: int):
        self.is_valid_date(day, month, year)
        self.day = day
        self.month = month
        self.year = year
        #self.is_valid_date(self._day, self._month, self._year)

    # TODO какой декоратор следует применить?
    @staticmethod
    def is_leap_year(year: int) -> bool:
        """Проверяет, является ли год високосным"""
        # TODO записать условие проверки високосного года
        if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
            return True
        else:
            False

    def get_max_day(self, month: int, year: int) -> int:
        """Возвращает максимальное количество дней в месяце для указанного года"""
        # TODO вернуть количество дней указанного месяца
        if self.is_leap_year(year):
            new_days = self.DAY_OF_MONTH[1]
            return new_days[month - 1]
        else:
            new_days = self.DAY_OF_MONTH[0]
            return new_days[month - 1]
    """@staticmethod
    def is_valid_date(day: int, month: int, year: int) -> None:
        #Проверяет, является ли дата корректной
        # TODO если указанный набор день, месяц и год неверны, то вызвать ошибку ValueError
        if not isinstance(day, (int, type(None))):
            raise TypeError()
        if not isinstance(month, (int, type(None))):
            raise TypeError()
        if not isinstance(year, (int, type(None))):
            raise TypeError()"""

    def is_valid_date(self, day, month, year) -> int:
        max_days = self.get_max_day(month, year)
        if 1 <= day <= max_days:
            return day
        else:
            raise ValueError("Некорректная дата")

    # TODO записать getter и setter для дня
    @property
    def day(self):
        return self._day

    @day.setter
    def day(self, day_: int):
        if not isinstance(day_, int):
            raise TypeError()
        else:
            self._day = day_

    # TODO записать getter и setter для года

    @property
    def month(self):
        return self._month

    @month.setter
    def month(self, month_: int):
        if not isinstance(month_, int):
            raise TypeError()
        if 1 <= month_ <= 12:
            self._month = month_
        else:
            raise ValueError()

    @property
    def year(self):
        return self._year

    @year.setter
    def year(self, year_: int):
        if not isinstance(year_, int):
            raise TypeError()
        if 0 <= year_ <= 2023:
            self._year = year_
        else:
            raise ValueError()


if __name__ == '__main__':

    date = Date(28, 2, 2020)
    date._Date__day = 1
    print(date.day)
    print(Date(29, 2, 2023))

