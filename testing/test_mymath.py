import unittest
import mymath


class TestMath(unittest.TestCase):
    def test_sum(self):
        self.assertEqual(mymath.sum(1,2),3)
        self.assertEqual(mymath.sum(1.1, 2.3), 3.4)

    def test_subtract(self):
        self.assertEqual(mymath.subtract(10, 2), 8)
        self.assertEqual(mymath.subtract(-3, 2), -5)

    def test_mul(self):
        self.assertEqual(mymath.mul(2,3), 6)
        self.assertEqual(mymath.mul(-1,-2), 2)

    def test_divide(self):
        self.assertEqual(mymath.divide(10, 2), 5)
        self.assertEqual(mymath.divide(3, 2), 1.5)
        self.assertRaises(ValueError, mymath.divide, 12, 0)


if __name__ == '__main__':
    unittest.main()
