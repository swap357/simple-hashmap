class HashMap:
    def __init__(self, size=100):
        self.size = size
        self.buckets = [[] for _ in range(size)]
    
    def _hash(self, key: str) -> int:
        return sum(ord(c) for c in key) % self.size
    
    def get(self, key: str) -> int | None:
        bucket = self._hash(key)
        for k, v in self.buckets[bucket]:
            if k == key:
                return v
        return None
    
    def set(self, key: str, value: int) -> None:
        bucket = self._hash(key)
        for i, (k, v) in enumerate(self.buckets[bucket]):
            if k == key:
                self.buckets[bucket][i] = (key, value)
                return
        self.buckets[bucket].append((key, value))
    
    def delete(self, key: str) -> None:
        bucket = self._hash(key)
        self.buckets[bucket] = [(k, v) for k, v in self.buckets[bucket] if k != key]

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


if __name__ == "__main__":
    main()