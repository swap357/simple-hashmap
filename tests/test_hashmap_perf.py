import timeit
import random
import string
from src.hashmap_v2 import HashMap

def generate_random_string(length):
    return ''.join(random.choice(string.ascii_letters) for _ in range(length))

def test_performance(data_structure, operation, size):
    data = [(generate_random_string(10), i) for i in range(size)]
    
    if operation == 'set':
        if isinstance(data_structure, HashMap):
            def test():
                for key, value in data:
                    data_structure.set(key, value)
        else:
            def test():
                for key, value in data:
                    data_structure[key] = value
    elif operation == 'get':
        if isinstance(data_structure, HashMap):
            for key, value in data:
                data_structure.set(key, value)
            def test():
                for key, _ in data:
                    _ = data_structure.get(key)
        else:
            for key, value in data:
                data_structure[key] = value
            def test():
                for key, _ in data:
                    _ = data_structure.get(key)
    elif operation == 'delete':
        if isinstance(data_structure, HashMap):
            for key, value in data:
                data_structure.set(key, value)
            def test():
                for key, _ in data:
                    data_structure.delete(key)
        else:
            for key, value in data:
                data_structure[key] = value
            def test():
                for key, _ in data:
                    del data_structure[key]
    else:
        raise ValueError("Invalid operation")
    
    return timeit.timeit(test, number=1)

def compare_performance(sizes):
    operations = ['set', 'get', 'delete']
    
    print(f"{'Size':<10}{'Operation':<10}{'HashMap':<15}{'dict':<15}{'built-in hash':<15}")
    print("-" * 65)
    
    for size in sizes:
        for operation in operations:
            hashmap_time = test_performance(HashMap(), operation, size)
            dict_time = test_performance({}, operation, size)
            
            # For built-in hash, we're just hashing the keys
            if operation == 'set':
                hash_time = timeit.timeit(lambda: [hash(key) for key, _ in [(generate_random_string(10), i) for i in range(size)]], number=1)
            else:
                hash_time = "N/A"
            
            print(f"{size:<10}{operation:<10}{hashmap_time:<15.6f}{dict_time:<15.6f}{hash_time:<15}")
        print("-" * 65)

if __name__ == '__main__':
    sizes = [100, 1000, 10000]
    compare_performance(sizes)