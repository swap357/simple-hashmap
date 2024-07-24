# simple-hashmap

This project implements a custom HashMap data structure in Python, along with unit tests and performance tests.

## Setup

1. Clone the repository:
   ```
   git clone https://github.com/swap357/simple-hashmap.git
   cd simple-hashmap
   ```

2. Create a virtual environment and activate it:
   ```
   python3 -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

## Running Tests

To run the unit tests:
```
python3 -m unittest tests.test_hashmap
```

To run the performance tests:
```
python3 -m tests.test_hashmap_perf
```

## Usage

You can use the HashMap in your own Python code like this:

```python
from src.hashmap import HashMap

m = HashMap()
m.set("num_dogs", 1)
m.set("num_cats", 3)
print(m.get("num_dogs"))  # 1
m.set("num_dogs", 2)
print(m.get("num_dogs"))  # 2
print(m.get("num_cats"))  # 3
m.delete("num_dogs")
print(m.get("num_dogs"))  # None
```