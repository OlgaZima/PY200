from abc import ABC, abstractmethod


class CheckAge:
    @abstractmethod
    def check_age(self):
        pass


class CheckDiscount:
    @abstractmethod
    def check_discount(self):
        pass


class CheckFilm:
    @abstractmethod
    def check_out(self):
        pass


class UpdateFilm:
    @abstractmethod
    def update(self):
        pass


class User(ABC):
    def __init__(self, login: str, phone: int):
        self.login = login
        self.phone = phone

    def __str__(self) -> str:
        return f'Пользователь {self.login}. Номер {self.phone}'


class User_const(User, CheckAge, CheckDiscount):
    def __init__(self, login: str, phone: int):
        super().__init__(login, phone)

    def check_age(self):
        return f'Уважаемый, {self.login}, вам доступны все фильмы'

    def check_discount(self):
        return 'Скидка постоянного пользователя составляет 25 %'


class User_occasional(User, CheckAge):
    def __init__(self, login: str, phone: int, age: int):
        super().__init__(login, phone)
        self.age = age

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age_):
        if not isinstance(age_, int):
            raise TypeError()
        if age_ < 3 or age_ > 150:
            raise ValueError()
        self._age = age_

    def check_age(self):
        if self.age < 18:
            return f'Уважаемый, {self.login}, некоторые фильмы недоступны для вас'
        if self.age >= 18:
            return f'Уважаемый, {self.login}, вам доступны любые фильмы'

    # def check_discount(self):
    #     pass

    def __str__(self) -> str:
        return f'{self.login}, {self.phone}, {self._age}'


class User_free(User, CheckAge, CheckDiscount):
    def __init__(self, login: str, phone: int):
        super().__init__(login, phone)

    def check_age(self):
        return f'Уважаемый, {self.login}, вам доступны все фильмы'

    def check_discount(self):
        return f'Уважаемый, {self.login}, как сотруднику компании, все фильмы для вас бесплатны'


class Film(ABC):
    def __init__(self, title: str, quality: str, size: float, rating: float):
        self.title = title
        self.quality = quality
        self.size = size
        self.rating = rating

    def __str__(self) -> str:
        return f'{self.title}, {self.quality}, {self.size}, {self.rating}'


class Film_online(Film, CheckFilm, UpdateFilm):
    def __init__(self, title: str, quality: str, size: float, rating: float, period=30):
        super().__init__(title, quality, size, rating)
        self.period = period

    def update(self, period_new: int):
        self.period = period_new

    def check_out(self):
        print(f'Фильм {self.title} доступен для просмотра в течение{self.period} дней')


class Film_download(Film):
    def __init__(self, title: str, quality: str, size: float, rating: float, link='www.example.com/film/'):
        super().__init__(title, quality, size, rating)
        self.link = link

    def update(self, link_new: str):
        self.link = link_new

    def check_out(self):
        print(f'Фильм {self.title} доступен для просмотра по ссылке {self.link}')


class User_repository:
    def __init__(self):
        self.users = []

    def add_users(self, user_):
        self.users.append(user_)

    def del_users(self, login_, phone_):
        for i in self.users:
            if i.login == login_ and i.phone == phone_:
                self.users.remove(i)

    def check_age(self, login_):
        for i in self.users:
            if i.login == login_ and isinstance(i, CheckAge):
                return i.check_age()
        print('Пользователь с таким логином не найден')

    def check_discount(self, login_):
        for i in self.users:
            if i.login == login_ and isinstance(i, CheckDiscount):
                return i.check_discount()
        print('Пользователь с таким логином не найден')

    def __str__(self):
        for i in self.users:
            return f'Пользователь {i.login}. Номер {i.phone}. Возраст {i.age}'


class Order:
    def __init__(self, order_id, login, title):
        self.order_id = order_id
        self.login = login
        self.title = title

    def __str__(self):
        return f'Номер заказа {self.order_id}. Пользователь {self.login}. Фильм {self.title}'


class Order_repository(CheckAge, CheckDiscount):
    def __init__(self):
        self.orders = []

    def add_orders(self, order_):
        self.orders.append(order_)

    def del_all_orders(self, login_):
        for i in self.orders:
            if i.login == login_:
                self.orders.remove(i)

    def del_title_orders(self, title_):
        for i in self.orders:
            if i.title == title_:
                self.orders.remove(i)

    def check_discount(self, login_):
        for i in self.orders:
            if i.login == login_:
                return f'Надо проверить скидку пользователя {i.login}'
        print('Пользователь с таким логином не найден')

    def check_age(self, login_):
        for i in self.orders:
            if i.login == login_:
                return f'Надо проверить возраст пользователя {i.login}'
        print('Пользователь с таким логином не найден')

    def __str__(self):
        for i in self.orders:
            return f'Номер заказа {i.order_id}. Пользователь {i.login}. Фильм {i.title}'


if __name__ == "__main__":
    user = User_repository()
    user1 = User_const("Zima", 1234)
    print(user1.check_age())
    user2 = User_free("Leto", 1234)
    user3 = User_occasional("Spring", 1234, 17)
    user.add_users(user1)
    user.add_users(user2)
    user.add_users(user3)
    print(user.check_discount('Leto'))
    order = Order_repository()
    order1 = Order(1, 'Spring', 'Happy')
    order2 = Order(2, 'Zima', 'New')
    order3 = Order(3, 'Zima', 'New')
    order.add_orders(order1)
    order.add_orders(order2)
    order.add_orders(order3)
    order.del_all_orders('Zima')
    film = Film_download('Night', 'HD', 10.2, 9.9)
    film = Film_download('Night', 'HD', 10.2, 9.9)
    film.update('www.example.com/film_rep/')
    print(film.link)








