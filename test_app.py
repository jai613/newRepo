# test_app.py
import unittest
from app import add_numbers, subtract_numbers

class TestApp(unittest.TestCase):
    def test_add_numbers(self):
        self.assertEqual(add_numbers(3, 5), 8)
        self.assertEqual(add_numbers(-3, 3), 0)

    def test_subtract_numbers(self):
        self.assertEqual(subtract_numbers(10, 5), 5)
        self.assertEqual(subtract_numbers(0, 7), -7)

if __name__ == "__main__":
    unittest.main()
