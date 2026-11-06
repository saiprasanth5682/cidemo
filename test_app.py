import unittest
from app import add_numbers, greet

class TestApp(unittest.TestCase):
    def test_add_numbers(self):
        self.assertEqual(add_numbers(10, 20), 30)

    def test_add_decimal_numbers(self):
        self.assertAlmostEqual(add_numbers(1.5, 2.5), 4.0)

    def test_greet(self):
        self.assertEqual(greet("Vijay"), "Hello, Vijay!")

    def test_greet_trims_whitespace(self):
        self.assertEqual(greet("  Vijay  "), "Hello, Vijay!")

    def test_greet_rejects_empty_name(self):
        with self.assertRaises(ValueError):
            greet("   ")

if __name__ == "__main__":
    unittest.main()
