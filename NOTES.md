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

```
python3 -m tests.test_hashmap
......
----------------------------------------------------------------------
Ran 6 tests in 0.002s

OK
```

```
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
```

# v2

- 'set' operation:

we modify the set() method for HashMap instead of item assignment.
It still uses item assignment for the built-in dict.


- 'get' operation:

we update the get() method for both HashMap and dict.
For HashMap, it uses set() to populate the data structure before testing.


- 'delete' operation:

It uses the delete() method for HashMap.
It still uses del for the built-in dict.
For HashMap, it uses set() to populate the data structure before testing.
```
python3 -m tests.test_hashmap     
......
----------------------------------------------------------------------
Ran 6 tests in 0.002s

OK
```

```
python3 -m tests.test_hashmap_perf
Size      Operation HashMap        dict           built-in hash  
-----------------------------------------------------------------
100       set       0.000147       0.000009       0.00026391702704131603
100       get       0.000023       0.000005       N/A            
100       delete    0.000044       0.000004       N/A            
-----------------------------------------------------------------
1000      set       0.001242       0.000060       0.0023848330602049828
1000      get       0.000175       0.000031       N/A            
1000      delete    0.000357       0.000029       N/A            
-----------------------------------------------------------------
10000     set       0.007723       0.000464       0.018800791003741324
10000     get       0.001451       0.000288       N/A            
10000     delete    0.003143       0.000239       N/A            
-----------------------------------------------------------------
```

# line by line profiling

Profile collected using -
```
python3 hashmap_profiler.py
```

### Line-by-line profiling:

```
Timer unit: 1e-09 s

Total time: 0.096324 s
File: /Users/swap357/july24/simple-hashmap/hashmap_profiler.py
Function: profile_hashmap at line 14

Line #      Hits         Time  Per Hit   % Time  Line Contents
==============================================================
    14                                           def profile_hashmap():
    15         1       4000.0   4000.0      0.0      m = HashMap()
    16                                               
    17                                               # Populate the HashMap
    18     10001    1089000.0    108.9      1.1      for i in range(10000):
    19     10000   80353000.0   8035.3     83.4          m.set(f"key_{i}", i)
    20                                               
    21                                               # Perform various operations
    22      5001     658000.0    131.6      0.7      for i in range(5000):
    23      5000    8479000.0   1695.8      8.8          m.get(f"key_{i}")
    24      1001     128000.0    127.9      0.1      for i in range(2000, 3000):
    25      1000    2504000.0   2504.0      2.6          m.delete(f"key_{i}")
    26      1001     114000.0    113.9      0.1      for i in range(5000, 6000):
    27      1000    2995000.0   2995.0      3.1          m.set(f"new_key_{i}", i)

Total time: 0.003763 s
File: /Users/swap357/july24/simple-hashmap/src/hashmap_v2.py
Function: get at line 10

Line #      Hits         Time  Per Hit   % Time  Line Contents
==============================================================
    10                                               def get(self, key: str) -> int | None:
    11      5000    1337000.0    267.4     35.5          bucket = self._hash(key)
    12      5808    1405000.0    241.9     37.3          for k, v in self.buckets[bucket]:
    13      5808     548000.0     94.4     14.6              if k == key:
    14      5000     473000.0     94.6     12.6                  return v
    15                                                   return None

Total time: 0.041941 s
File: /Users/swap357/july24/simple-hashmap/src/hashmap_v2.py
Function: set at line 17

Line #      Hits         Time  Per Hit   % Time  Line Contents
==============================================================
    17                                               def set(self, key: str, value: int) -> None:
    18     23282   16754000.0    719.6     39.9          self._resize_if_needed()
    19     23282    7191000.0    308.9     17.1          bucket = self._hash(key)
    20     31695    8352000.0    263.5     19.9          for i, (k, v) in enumerate(self.buckets[bucket]):
    21      8413     915000.0    108.8      2.2              if k == key:
    22                                                           self.buckets[bucket][i] = (key, value)
    23                                                           return
    24     23282    4675000.0    200.8     11.1          self.buckets[bucket].append((key, value))
    25     23282    4054000.0    174.1      9.7          self.count += 1

Total time: 0.0014 s
File: /Users/swap357/july24/simple-hashmap/src/hashmap_v2.py
Function: delete at line 27

Line #      Hits         Time  Per Hit   % Time  Line Contents
==============================================================
    27                                               def delete(self, key: str) -> None:
    28      1000     308000.0    308.0     22.0          bucket = self._hash(key)
    29      1000     515000.0    515.0     36.8          new_bucket = [(k, v) for k, v in self.buckets[bucket] if k != key]
    30      1000     242000.0    242.0     17.3          if len(new_bucket) != len(self.buckets[bucket]):
    31      1000     160000.0    160.0     11.4              self.count -= 1
    32      1000     175000.0    175.0     12.5          self.buckets[bucket] = new_bucket

Total time: 0.006381 s
File: /Users/swap357/july24/simple-hashmap/src/hashmap_v2.py
Function: _resize_if_needed at line 34

Line #      Hits         Time  Per Hit   % Time  Line Contents
==============================================================
    34                                               def _resize_if_needed(self):
    35     23282    3583000.0    153.9     56.2          if self.count >= self.size * 0.75:
    36        11    2798000.0 254363.6     43.8              self._resize(self.size * 2)

Total time: 0.04206 s
File: /Users/swap357/july24/simple-hashmap/src/hashmap_v2.py
Function: _resize at line 38

Line #      Hits         Time  Per Hit   % Time  Line Contents
==============================================================
    38                                               def _resize(self, new_size):
    39        11          0.0      0.0      0.0          old_buckets = self.buckets
    40        11          0.0      0.0      0.0          self.size = new_size
    41        11    2757000.0 250636.4      6.6          self.buckets = [[] for _ in range(self.size)]
    42        11       2000.0    181.8      0.0          self.count = 0
    43     16387    2104000.0    128.4      5.0          for bucket in old_buckets:
    44     28658    4257000.0    148.5     10.1              for k, v in bucket:
    45     12282   32940000.0   2682.0     78.3                  self.set(k, v)
```


### Memory profiling:
```
Peak memory usage: 50.78125 MiB
```

### Time profiling:
```
         137436 function calls (112872 primitive calls) in 0.046 seconds

   Ordered by: cumulative time

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.003    0.003    0.046    0.046 /Users/swap357/july24/simple-hashmap/hashmap_profiler.py:14(profile_hashmap)
23282/11000    0.015    0.000    0.039    0.000 /Users/swap357/july24/simple-hashmap/src/hashmap_v2.py:17(set)
23282/11000    0.003    0.000    0.029    0.000 /Users/swap357/july24/simple-hashmap/src/hashmap_v2.py:34(_resize_if_needed)
       11    0.003    0.000    0.027    0.002 /Users/swap357/july24/simple-hashmap/src/hashmap_v2.py:38(_resize)
       11    0.012    0.001    0.012    0.001 /Users/swap357/july24/simple-hashmap/src/hashmap_v2.py:41(<listcomp>)
    29282    0.004    0.000    0.006    0.000 /Users/swap357/july24/simple-hashmap/src/hashmap_v2.py:7(_hash)
     5000    0.001    0.000    0.002    0.000 /Users/swap357/july24/simple-hashmap/src/hashmap_v2.py:10(get)
    29282    0.001    0.000    0.001    0.000 {built-in method builtins.hash}
     1000    0.001    0.000    0.001    0.000 /Users/swap357/july24/simple-hashmap/src/hashmap_v2.py:27(delete)
    23282    0.001    0.000    0.001    0.000 {method 'append' of 'list' objects}
     1000    0.000    0.000    0.000    0.000 /Users/swap357/july24/simple-hashmap/src/hashmap_v2.py:29(<listcomp>)
     2000    0.000    0.000    0.000    0.000 {built-in method builtins.len}
        1    0.000    0.000    0.000    0.000 /Users/swap357/july24/simple-hashmap/src/hashmap_v2.py:2(__init__)
        1    0.000    0.000    0.000    0.000 /Users/swap357/july24/simple-hashmap/src/hashmap_v2.py:4(<listcomp>)
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
```

## Observations

set
- consumes 83.4% of total time, averaging ~8035 ns per call
- optimizing resizing strategy might help, load factor needs to be adjusted for use-case and based on prod data.

resize
- Most time-consuming operation: self.set(k, v) calls (78.3% of _resize() time)
- is expensive and on critical code path, solutions - predictive resizing (pre-resize based on load factor), lazy resizing (resize on get/delete)

get
- relatively fast
- Time distribution:
  - Hash calculation (35.5%)
  - Bucket traversal (37.3%)
  - Key comparison (14.6%)
