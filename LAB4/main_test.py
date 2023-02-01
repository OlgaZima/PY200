import unittest
from main import Library  # импортируем то, что будем тестировать


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.library1 = Library('Night', 'Gogol', 123, 1900)
        self.library2 = Library('Night', 'Gogol', 123, 1902)

    def test_name(self):
        self.assertEqual(self.library1.name, 'Night')  # add assertion here

    def test_author(self):
        self.assertEqual(self.library1.author, 'Gogol')

    def test_pages(self):
        self.assertEqual(self.library1.pages, 123)

    def test_year(self):
        self.assertEqual(self.library2.year, 1902)

    def test_check_id(self):
        self.assertTrue((self.library1.name == self.library2.name and
                         self.library1.author == self.library2.author), msg=True)

    def test_add_book_count(self):
        self.assertEqual(self.library1.book_count, 2)


if __name__ == '__main__':
    unittest.main()



