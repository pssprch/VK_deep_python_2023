import unittest
from dsc import Finance


class TestDescriptors(unittest.TestCase):

    def test_positive_value(self):
        finance = Finance(1000, 5, 3)
        finance.principal = 2000

        with self.assertRaises(ValueError):
            finance.principal = -1

        self.assertEqual(finance.principal, 2000)
        del finance.principal

    def test_two_values(self):
        finance = Finance(1000, 5, 3, 1500)
        self.assertEqual(finance.principal, 1000)
        self.assertEqual(finance.amount, 1500)
        finance.principal = 2000
        finance.amount = 2500

        self.assertEqual(finance.principal, 2000)
        self.assertEqual(finance.amount, 2500)
        self.assertEqual(finance.principal, 2000)
        self.assertEqual(finance.amount, 2500)

        with self.assertRaises(ValueError):
            finance.principal = -1
        with self.assertRaises(ValueError):
            finance.amount = -1

    def test_rate(self):
        finance = Finance(1000, 5, 3)
        finance.r = 50
        self.assertEqual(finance.r, 50)

        with self.assertRaises(ValueError):
            finance.r = -1
        with self.assertRaises(ValueError):
            finance.r = 101
        del finance.r

    def test_time(self):
        finance = Finance(1000, 5, 3)
        finance.t = 4
        self.assertEqual(finance.t, 4)

        with self.assertRaises(TypeError):
            finance.t = "3"
        with self.assertRaises(TypeError):
            finance.t = 2.5
        del finance.t

    def test_compound_interest(self):
        finance = Finance(1000, 5, 3)
        expected = 1000 * ((1 + 5 / 100) ** 3) - 1000
        self.assertAlmostEqual(finance.compound_interest(), expected, places=2)


if __name__ == "__main__":
    unittest.main()
