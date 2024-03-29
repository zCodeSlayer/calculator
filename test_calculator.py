import unittest
from calculator import calculator


class CalculatorTest(unittest.TestCase):
    def test_plus(self):
        self.assertEqual(calculator('1+6'), 7)

    def test_minus(self):
        self.assertEqual(calculator('7-3'), 4)

    def test_multiply(self):
        self.assertEqual(calculator('3*6'), 18)

    def test_devide(self):
        self.assertEqual(calculator('10/2'), 5)

    def test_mod(self):
        self.assertEqual(calculator('11%2'), 1)

    def test_no_signs(self):
        with self.assertRaises(ValueError) as e:
            calculator('fbdhfjsjvdfhsdf')
        self.assertEqual('Выражение должно содержать хотя бы один знак (+-/*%)', e.exception.args[0])

    def test_two_signs(self):
        with self.assertRaises(ValueError) as e:
            calculator('2+2+2')
        self.assertEqual('Выражение должно содержать два целых числа и один знак (+-/*%)', e.exception.args[0])

    def test_many_signs(self):
        with self.assertRaises(ValueError) as e:
            calculator('2+3%1')
        self.assertEqual('Выражение должно содержать два целых числа и один знак (+-/*%)', e.exception.args[0])

    def test_no_inits(self):
        with self.assertRaises(ValueError) as e:
            calculator('2.2+3.0')
        self.assertEqual('Выражение должно содержать два целых числа и один знак (+-/*%)', e.exception.args[0])

    def test_string(self):
        with self.assertRaises(ValueError) as e:
            calculator('a+b')
        self.assertEqual('Выражение должно содержать два целых числа и один знак (+-/*%)', e.exception.args[0])


if __name__ == '__main__':
    unittest.main()
