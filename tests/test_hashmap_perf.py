import timeit
from src.hashmap import HashMap

def test_set_performance():
    hashmap = HashMap()
    def set_items():
        for i in range(10000):
            hashmap.set(f"key{i}", i)
    return timeit.timeit(set_items, number=1)

def test_get_performance():
    hashmap = HashMap()
    for i in range(10000):
        hashmap.set(f"key{i}", i)
    def get_items():
        for i in range(10000):
            hashmap.get(f"key{i}")
    return timeit.timeit(get_items, number=1)

def test_delete_performance():
    hashmap = HashMap()
    for i in range(10000):
        hashmap.set(f"key{i}", i)
    def delete_items():
        for i in range(10000):
            hashmap.delete(f"key{i}")
    return timeit.timeit(delete_items, number=1)

if __name__ == '__main__':
    print(f"Set performance: {test_set_performance():.4f} seconds")
    print(f"Get performance: {test_get_performance():.4f} seconds")
    print(f"Delete performance: {test_delete_performance():.4f} seconds")