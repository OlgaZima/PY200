import unittest
from main import User_repository, User_const, User_occasional, User_free, Film_online, Film_download, Order, Order_repository  # импортируем то, что будем тестировать


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.user1 = User_const('Nightmare', 1234, 17)
        self.user2 = User_occasional('Nick', 5678, 18)
        self.user3 = User_free('Bob', 1011)
        self.user = User_repository()
        self.user.add_users(self.user1)
        self.user.add_users(self.user2)
        self.user.add_users(self.user3)
        self.film1 = Film_online('Night', 'HD', 10.2, 25)
        self.film2 = Film_download('Night', 'HD', 10.2, 'www.example.com/film_rep/')
        self.film1.update(30)
        self.film2.update('www.example.com/film_rep/')
        self.order = Order_repository()
        self.order1 = Order(1, 'Spring', 'Happy')
        self.order2 = Order(2, 'Zima', 'New')
        self.order3 = Order(3, 'Zima', 'New')
        self.order.add_orders(self.order1)
        self.order.add_orders(self.order2)
        self.order.add_orders(self.order3)
        #self.order.del_all_orders('Zima')

    def test_login(self):
        self.assertEqual(self.user3.login, 'Bob')  # add assertion here

    def test_phone(self):
        self.assertEqual(self.user1.phone, 1234)

    def test_age(self):
        self.assertEqual(self.user1.check_age(), f'Уважаемый, {self.user1.login}, некоторые фильмы недоступны для вас')

    def test_user(self):
        self.assertEqual(self.user.count, 3)

    def test_period(self):
        self.assertEqual(self.film1.period, 30)

    def test_link(self):
        self.assertEqual(self.film2.link, 'www.example.com/film_rep/')

    def test_check_id(self):
        self.assertTrue((self.film1.title == self.film2.title and
                         self.film1.quality == self.film2.quality and
                         self.film1.size == self.film2.size), msg=True)

    def test_order_check_age(self):
        self.assertEqual(self.order.check_age('Spring'), f'Надо проверить возраст пользователя Spring')


if __name__ == '__main__':
    unittest.main()
