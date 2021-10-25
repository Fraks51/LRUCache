import unittest
from lru_cache import LRUCache
import random


little_dict = {"a": 1, "b": 2, "c": 3,
               "d": 4, "e": 5}
big_dict = {i: i for i in range(1000)}

class TestLRUCache(unittest.TestCase):

    def test_as_dict_default(self):
        default_lru_cache = LRUCache()
        for key, value in little_dict.items():
            default_lru_cache.add(key, value)
        self.assertEqual(default_lru_cache.get("e"), 5)
        self.assertEqual(default_lru_cache.get("b"), 2)
        self.assertIsNone(default_lru_cache.get("r"))
        self.assertIsNone(default_lru_cache.get(1))
        default_lru_cache.add("a", 33)
        self.assertEqual(default_lru_cache.get("a"), 33)
        default_lru_cache.add("r", 3)
        self.assertEqual(default_lru_cache.get("r"), 3)

    def test_cache(self):
        big_lru_cache = LRUCache(max_size=1000)
        for key, value in big_dict.items():
            big_lru_cache.add(key, value)
        big_lru_cache.add(1001, 1001)
        self.assertIsNone(big_lru_cache.get(0))
        big_lru_cache.add(1, 1)
        self.assertEqual(big_lru_cache.get(1), 1)
        big_lru_cache.add(1002, 1002)
        self.assertEqual(big_lru_cache.get(1), 1)
        self.assertIsNone(big_lru_cache.get(2))
        self.assertEqual(big_lru_cache.get(1001), 1001)
        for i in range(100):
            big_lru_cache.add(1003 + i, 1003 + i)
        self.assertEqual(big_lru_cache.get(1), 1)

        for i in range(100):
            self.assertIsNone(big_lru_cache.get(3 + i))
            self.assertEqual(big_lru_cache.get(1003 + i), 1003 + i)

    def test_as_dict_random(self):
        lru_cache = LRUCache(max_size=1000)
        default_dict = {}
        for _ in range(1000):
            key = random.randint(-100000, 1000000)
            value = random.randint(-100000, 1000000)
            default_dict[key] = value
            lru_cache.add(key, value)

        for key, value in default_dict.items():
            self.assertEqual(lru_cache.get(key), default_dict[key])


if __name__ == '__main__':
    unittest.main()
