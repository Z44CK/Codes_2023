import unittest
from Fibonacci import FibonacciGenerator


class TestFibonacciGenerator(unittest.TestCase):

    def test_init(self):
        fibonacci = FibonacciGenerator(5)
        self.assertEqual(fibonacci.iteracao, 5)
        self.assertEqual(fibonacci.anterior, 0)
        self.assertEqual(fibonacci.proximo, 1)

    def test_iter(self):
        fibonacci = FibonacciGenerator(5)
        self.assertEqual(iter(fibonacci), fibonacci)

    def test_next(self):
        fibonacci = FibonacciGenerator(5)
        self.assertEqual(next(fibonacci), 0)
        self.assertEqual(next(fibonacci), 1)
        self.assertEqual(next(fibonacci), 1)
        self.assertEqual(next(fibonacci), 2)
        self.assertEqual(next(fibonacci), 3)
        with self.assertRaises(StopIteration):
            next(fibonacci)


if __name__ == '__main__':
    unittest.main()
