import unittest

from list import CustomList


class TestCustomList(unittest.TestCase):

    def test_add(self):
        cl1 = CustomList([1, 2, 3, 4, 5])
        cl2 = CustomList([3, 3])
        cl3 = CustomList()
        lst = [-7, 1]

        self.assertEqual(cl1 + cl2, CustomList([4, 5, 3, 4, 5]))
        self.assertEqual(cl2 + cl1, CustomList([4, 5, 3, 4, 5]))
        self.assertEqual(cl1 + cl3, CustomList([1, 2, 3, 4, 5]))
        self.assertEqual([1, 2, 3, 4, 5], CustomList([1, 2, 3, 4, 5]))
        self.assertEqual(cl2 + cl3, CustomList([3, 3]))
        self.assertIsInstance(cl2 + lst, CustomList)
        self.assertIsInstance(lst + cl2, CustomList)
        self.assertEqual(cl2 + lst, [-4, 4])
        self.assertEqual(lst + cl2, [-4, 4])

    def test_sub(self):
        cl1 = CustomList([1, 2, 3, 4, 5, 6])
        cl2 = CustomList([2, 5, -7])
        cl3 = CustomList()
        lst = [-3, 1, 2]

        self.assertEqual(cl1 - cl2, CustomList([-1, -3, 10, 4, 5, 6]))
        self.assertEqual(cl2 - cl1, CustomList([1, 3, -10, -4, -5, -6]))
        self.assertEqual(cl1 - cl3, CustomList([1, 2, 3, 4, 5, 6]))
        self.assertEqual(cl3 - cl1, CustomList([-1, -2, -3, -4, -5, -6]))
        self.assertEqual(cl2 - cl3, CustomList([2, 5, -7]))
        self.assertEqual(cl3 - cl2, CustomList([-2, -5, 7]))
        self.assertIsInstance(cl1 - lst, CustomList)
        self.assertIsInstance(lst - cl1, CustomList)
        self.assertEqual(cl1 - lst, CustomList([4, 1, 1, 4, 5, 6]))
        self.assertEqual(lst - cl1, CustomList([-4, -1, -1, -4, -5, -6]))

    def test_comp(self):
        cl1 = CustomList([1, 2, 3, 4])
        cl2 = CustomList([1, 2, 3, 4])

        self.assertEqual(cl1, cl2)
        self.assertLessEqual(cl1, cl2)
        self.assertGreaterEqual(cl1, cl2)

        cl1 = CustomList([1, 2, 3, 4, -5])
        cl2 = CustomList([1, 2, 3, 5, -6])

        self.assertEqual(cl1, cl2)
        self.assertLessEqual(cl1, cl2)
        self.assertGreaterEqual(cl1, cl2)

        cl1 = CustomList([-6, -7, -8])
        cl2 = CustomList([1])

        self.assertLess(cl1, cl2)
        self.assertLessEqual(cl1, cl2)
        self.assertNotEqual(cl1, cl2)
        self.assertGreater(cl2, cl1)
        self.assertGreaterEqual(cl2, cl1)
        self.assertNotEqual(cl2, cl1)

    def test_str(self):
        cl1 = CustomList([1, 2, 3, 4, 5])
        cl2 = CustomList([])
        cl3 = CustomList([-3, -2, -1])

        self.assertEqual(str(cl1), "List: [1, 2, 3, 4, 5], Sum: 15")
        self.assertEqual(str(cl2), "List: [], Sum: 0")
        self.assertEqual(str(cl3), "List: [-3, -2, -1], Sum: -6")


if __name__ == '__main__':
    unittest.main()
