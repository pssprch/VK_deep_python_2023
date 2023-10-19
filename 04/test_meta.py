import unittest
from meta import CustomClass


class TestCustomMetaClass(unittest.TestCase):

    def test_attributes(self):
        inst = CustomClass()
        self.assertEqual(inst.custom_x, 50)
        self.assertEqual(inst.custom_line(), 100)
        self.assertEqual(inst.custom_val, 99)
        self.assertEqual(str(inst), "Custom_by_metaclass")

        self.assertTrue(hasattr(CustomClass, 'custom_x'))
        self.assertTrue(hasattr(CustomClass, 'custom_line'))

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

    def test_attribute_access_error(self):
        inst = CustomClass()
        with self.assertRaises(AttributeError):
            _ = inst.x
        with self.assertRaises(AttributeError):
            _ = inst.val
        with self.assertRaises(AttributeError):
            _ = inst.line
        with self.assertRaises(AttributeError):
            _ = inst.yyy
        with self.assertRaises(AttributeError):
            _ = inst.dynamic

    def test_instance_creation_asserts(self):
        inst = CustomClass()
        self.assertEqual(inst.custom_x, 50)
        self.assertEqual(inst.custom_val, 99)
        self.assertEqual(inst.custom_line(), 100)
        self.assertEqual(str(inst), "Custom_by_metaclass")


if __name__ == '__main__':
    unittest.main()
