import unittest


def add_numbers(a, b):
    return a + b

class TestMathOperations(unittest.TestCase):

    def test_add_numbers(self):
        self.assertEqual(add_numbers(2, 3), 5)

if __name__ == "__main__":
    unittest.main()
