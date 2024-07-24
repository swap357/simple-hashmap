import unittest
from src.hashmap import HashMap

class TestHashMap(unittest.TestCase):
    def setUp(self):
        self.hashmap = HashMap()

    def test_set_and_get(self):
        self.hashmap.set("key1", 1)
        self.assertEqual(self.hashmap.get("key1"), 1)

    def test_update_existing_key(self):
        self.hashmap.set("key1", 1)
        self.hashmap.set("key1", 2)
        self.assertEqual(self.hashmap.get("key1"), 2)

    def test_delete(self):
        self.hashmap.set("key1", 1)
        self.hashmap.delete("key1")
        self.assertIsNone(self.hashmap.get("key1"))

    def test_get_nonexistent_key(self):
        self.assertIsNone(self.hashmap.get("nonexistent"))

    def test_delete_nonexistent_key(self):
        self.hashmap.delete("nonexistent")  # Should not raise an exception

    def test_large_number_of_items(self):
        for i in range(1000):
            self.hashmap.set(f"key{i}", i)
        for i in range(1000):
            self.assertEqual(self.hashmap.get(f"key{i}"), i)

if __name__ == '__main__':
    unittest.main()