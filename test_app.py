import unittest

from app import greet


class TestGreet(unittest.TestCase):
    def test_greet_with_name(self):
        self.assertEqual(greet("Python"), "Hello, Python!")


if __name__ == "__main__":
    unittest.main()
