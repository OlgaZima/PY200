import hashlib
import random


class IdCounter:
    def __init__(self):
        self._id = 0

    def add_id(self):
        self._id += 1
        #return self._id

    # @property
    # def get_new_id(self):
    #     return self._id

    def get_new_id(self):
        self.add_id()
        return self._id


class Password:

    @classmethod
    def get(cls, password):
        if cls.is_valid(password):
            return hashlib.sha256(password.encode()).hexdigest()
        raise TypeError()

    @classmethod
    def check(cls, password: str, hash_password: str):
        if isinstance(hash_password, str):
            return cls.get(password) == hash_password
        raise TypeError('Хэш пароля должен быть строкой')

    @staticmethod
    def is_valid(password: str):
        if not isinstance(password, str):
            raise TypeError("Пароль должен быть строкой")
        assert len(password) > 8, "Пароль не менее 8 символов"
            #raise ValueError("Пароль не менее 8 символов")
        if password.isalpha() or password.isdigit():
            raise ValueError("Пароль должен состоять из букв и цифр")
        return True


class Product:
    counter = IdCounter()

    def __init__(self, name: str, price, rating):
        self._id = self.counter.get_new_id()
        self._name = None
        self.set_name(name)
        self.price = price
        self.rating = rating

    @property
    def id(self):
        return self._id

    @property
    def name(self):
        return self._name

    def set_name(self, n):
        if not isinstance(n, str):
            raise TypeError("Имя должно быть строкой")
        self._name = n

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, price_):
        if not isinstance(price_, float):
            if isinstance(price_, int):
                price_ = float(price_)
            else:
                raise TypeError()
        if price_ < 0:
            raise ValueError()
        self._price = price_

    @property
    def rating(self):
        return self._rating

    @rating.setter
    def rating(self, rating_):
        if not isinstance(rating_, float):
            raise TypeError()
        if rating_ < 0:
            raise ValueError("Должно быть положительное число")
        self._rating = rating_

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name}, price={self.price}, rating={self.rating})"

    def __str__(self):
        return f"{self.id}_{self.name}"


class Cart:
    def __init__(self):
        self.carts = []

    def add_products(self, p: Product):
        self.carts.append(p)

    def del_products(self, p: Product):
        self.carts.remove(p)

    def get_carts(self):
        return self.carts


class User:
    counter = IdCounter()

    def __init__(self, name, password):
        self._id = self.counter.get_new_id()
        self._name = None
        self.set_name(name)
        self.__password = Password.get(password)
        self._cart = Cart()

    def set_name(self, n):
        if not isinstance(n, str):
            raise TypeError
        self._name = n

    @property
    def cart(self):
        return self._cart

    @property
    def name(self):
        return self._name

    def __str__(self):
        return f"(id={self._id}, name={self.name})"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name}, password={self.password}"


class Generator:
    pr = ['Мыло', 'Порошок', 'Паста', 'Растворитель', 'Пятновыводитель', 'Файри']

    def get_pr(self):
        return random.choice(self.pr)

    def get_rating(self):
        return round(random.uniform(0, 5), 2)

    def get_price(self):
        return round(random.uniform(1, 5000), 2)

    def get_product(self):
        return Product(self.get_pr(), self.get_price(), self.get_rating())


class Store:
    def __init__(self, product_generator: Generator):
        self.user = None
        self.authentification()
        self.product_generator = product_generator

    def authentification(self):
        while True:
            login = input("Введите логин: ")
            password = input("Введите пароль: ")

            try:
                self.user = User(login, password)
                break
            except Exception as e:
                print(e)

    def add_to_cart(self):
        product = self.product_generator.get_product()
        print(product)
        self.user.cart.add_products(product)

    def view_cart(self):
        print(self.user.cart.get_carts())


if __name__ == "__main__":
    s = Store(Generator())
    s.add_to_cart()
    s.add_to_cart()
    s.add_to_cart()
    s.add_to_cart()
    s.view_cart()

