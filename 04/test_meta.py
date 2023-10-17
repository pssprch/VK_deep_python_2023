import unittest
from meta import CustomClass


class TestCustomMetaClass(unittest.TestCase):

    def test_attributes(self):
        inst = CustomClass()
        self.assertEqual(inst.custom_x, 50)
        self.assertEqual(inst.custom_line(), 100)
        self.assertEqual(inst.custom_val, 99)
        self.assertEqual(str(inst), "Custom_by_metaclass")

    def test_dynamic_attributes(self):
        inst = CustomClass()
        inst.dynamic = "added later"
        self.assertEqual(inst.custom_dynamic, "added later")
        inst.dynamic = 12
        self.assertEqual(inst.custom_dynamic, 12)

    def test_attribute_not_present(self):
        inst = CustomClass()
        with self.assertRaises(AttributeError):
            _ = inst.custom_not_present


if __name__ == '__main__':
    unittest.main()
