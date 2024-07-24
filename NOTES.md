# v1

## Hash Function

- Implements a simple, efficient hash function:
  ```python
  def _hash(self, key: str) -> int:
      return sum(ord(c) for c in key) % self.size
  ```

### Get
- Find the bucket the key is in using the hash function.
- Search for the key in the bucket (linear search).
- Time complexity: O(1) average case, O(n) worst case (if all keys hash to the same bucket).

### Set
- Find the bucket the key should be in using the hash function.
- Search for the key in the bucket:
  - If the key is not in the bucket, add it.
  - If the key is in the bucket, update its value.
- Time complexity: O(1) average case, O(n) worst case.

### Delete
- Find the bucket the key is in using the hash function.
- Remove the key-value pair from the bucket.
- Slightly tricky as we need to handle the case where the key doesn't exist.
- Time complexity: O(1) average case, O(n) worst case.

# references: 
- https://runestone.academy/ns/books/published/pythonds/SortSearch/Hashing.html
- https://stephenagrice.medium.com/how-to-implement-a-hash-table-in-python-1eb6c55019fd
- https://ksvi.mff.cuni.cz/~dingle/2021-2/algs/notes_11.html

python3 -m tests.test_hashmap
......
----------------------------------------------------------------------
Ran 6 tests in 0.002s

OK

python3 -m tests.test_hashmap_perf
Size      Operation HashMap        dict           built-in hash  
-----------------------------------------------------------------
100       set       0.000085       0.000009       0.00026154203806072474
100       get       0.000071       0.000005       N/A            
100       delete    0.000081       0.000004       N/A            
-----------------------------------------------------------------
1000      set       0.000853       0.000062       0.0023665830958634615
1000      get       0.000678       0.000031       N/A            
1000      delete    0.000862       0.000026       N/A            
-----------------------------------------------------------------
10000     set       0.015775       0.000497       0.018132915953174233
10000     get       0.012161       0.000310       N/A            
10000     delete    0.021422       0.000245       N/A            
-----------------------------------------------------------------

# v2


