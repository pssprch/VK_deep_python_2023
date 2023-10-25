import unittest
from lru_cache import LRUCache


class TestLRUCache(unittest.TestCase):

    def test_set_and_get(self):
        cache = LRUCache(2)

        cache.set('a', 1)
        cache.set('b', 2)
        self.assertEqual(cache.get('a'), 1)
        self.assertEqual(cache.get('b'), 2)

        cache.set("k1", "val1")
        cache.set("k2", "val2")
        self.assertEqual(cache.get("k2"), "val2")
        self.assertEqual(cache.get("k1"), "val1")
        self.assertEqual(cache.get("k3"), None)

        cache.set("k3", "val3")
        self.assertEqual(cache.get("k3"), "val3")
        self.assertEqual(cache.get("k2"), None)
        self.assertEqual(cache.get("k1"), "val1")

    def test_lru_eviction(self):
        cache = LRUCache(2)

        cache.set('a', 1)
        cache.set('b', 2)
        cache.set('c', 3)
        self.assertIsNone(cache.get('a'))
        self.assertEqual(cache.get('b'), 2)
        self.assertEqual(cache.get('c'), 3)

    def test_update_value(self):
        cache = LRUCache(2)

        cache.set('a', 1)
        cache.set('a', 2)
        self.assertEqual(cache.get('a'), 2)

    def test_limit(self):
        with self.assertRaises(ValueError):
            LRUCache(-1)
        with self.assertRaises(ValueError):
            LRUCache(10000)

    def test_set_exceed_limit(self):
        cache = LRUCache(1)

        cache.set('a', 1)
        cache.set('b', 2)
        self.assertIsNone(cache.get('a'))
        self.assertEqual(cache.get('b'), 2)

    def test_get_non_existent_key(self):
        cache = LRUCache(2)
        self.assertIsNone(cache.get('a'))

    def test_ordering_after_get(self):
        cache = LRUCache(2)

        cache.set('a', 1)
        cache.set('b', 2)
        cache.get('a')
        cache.set('c', 3)
        self.assertIsNone(cache.get('b'))
        self.assertEqual(cache.get('a'), 1)
        self.assertEqual(cache.get('c'), 3)


if __name__ == '__main__':
    unittest.main()
