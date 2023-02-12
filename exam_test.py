import random
import unittest
import hashlib

from exam import IdCounter, Password, User, Cart, Product


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self._id = IdCounter()
        self.password = Password()
        self.user = User('Vasya', '123456qwe')
        self.user.set_name('Vasy')
        self.price = round(random.uniform(1, 5000), 2)
        self.pr = ['Мыло', 'Порошок', 'Паста', 'Растворитель', 'Пятновыводитель', 'Файри']

    def test_id(self):
        self.assertEqual(self._id.get_new_id(), 1)

    def test_password_check(self):
        self.assertEqual(self.password.get(password='123456kkk'), hashlib.sha256('123456kkk'.encode()).hexdigest())

    def test_password_is_valid_1(self):
        self.assertRaises(ValueError, self.password.is_valid, '111111111')

    def test_password_is_valid_2(self):
        self.assertRaises(AssertionError, self.password.is_valid, '123lkj')

    def test_user_login(self):
        self.assertTrue(self.user.name, 'Vasya')

    def test_user_password(self):
        self.assertTrue(self.user.name, '123456qwe')

    def test_user_set_name(self):
        self.assertTrue(self.user.set_name, 'Vasy')

    def test_user_set_name(self):
        self.assertRaises(TypeError, self.user.set_name, 111)

    def test_product(self):
        for i in random.sample(self.pr, 5):
            self.assertTrue(i in self.pr)


