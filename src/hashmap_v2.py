class HashMap:
    def __init__(self, size=8):
        self.size = size
        self.buckets = [[] for _ in range(size)]
        self.count = 0

    def _hash(self, key: str) -> int:
        return hash(key) % self.size

    def get(self, key: str) -> int | None:
        bucket = self._hash(key)
        for k, v in self.buckets[bucket]:
            if k == key:
                return v
        return None

    def set(self, key: str, value: int) -> None:
        self._resize_if_needed()
        bucket = self._hash(key)
        for i, (k, v) in enumerate(self.buckets[bucket]):
            if k == key:
                self.buckets[bucket][i] = (key, value)
                return
        self.buckets[bucket].append((key, value))
        self.count += 1

    def delete(self, key: str) -> None:
        bucket = self._hash(key)
        new_bucket = [(k, v) for k, v in self.buckets[bucket] if k != key]
        if len(new_bucket) != len(self.buckets[bucket]):
            self.count -= 1
        self.buckets[bucket] = new_bucket

    def _resize_if_needed(self):
        if self.count >= self.size * 0.75:
            self._resize(self.size * 2)

    def _resize(self, new_size):
        old_buckets = self.buckets
        self.size = new_size
        self.buckets = [[] for _ in range(self.size)]
        self.count = 0
        for bucket in old_buckets:
            for k, v in bucket:
                self.set(k, v)

def main():
    # Example usage
    m = HashMap()
    m.set("num_dogs", 1)
    m.set("num_cats", 3)
    print(m.get("num_dogs"))  # 1
    m.set("num_dogs", 2)
    print(m.get("num_dogs"))  # 2
    print(m.get("num_cats"))  # 3
    m.delete("num_dogs")
    print(m.get("num_dogs"))  # None
    
    # Test resizing
    for i in range(100):
        m.set(f"key_{i}", i)
    print(f"Size after adding 100 items: {m.size}")

if __name__ == "__main__":
    main()