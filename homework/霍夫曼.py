class HashMap:
    def __init__(self, size):
        self.size = size
        self.slots = [None] * self.size
        self.data = [None] * self.size

    def hash_function(self, key):
        return hash(key) % self.size

    def rehash(self, old_hash):
        return (old_hash + 1) % self.size

    def put(self, key, value):
        hash_value = self.hash_function(key)

        if self.slots[hash_value] is None:
            self.slots[hash_value] = key
            self.data[hash_value] = value
        else:
            if self.slots[hash_value] == key:
                self.data[hash_value] = value
            else:
                next_slot = self.rehash(hash_value)
                while self.slots[next_slot] is not None and self.slots[next_slot] != key:
                    next_slot = self.rehash(next_slot)
                    if next_slot == hash_value:
                        raise ValueError("HashMap is full")
                if self.slots[next_slot] is None:
                    self.slots[next_slot] = key
                    self.data[next_slot] = value
                else:
                    self.data[next_slot] = value

    def get(self, key):
        start_slot = self.hash_function(key)

        value = None
        found = False
        stop = False
        position = start_slot

        while self.slots[position] is not None and not found and not stop:
            if self.slots[position] == key:
                found = True
                value = self.data[position]
            else:
                position = self.rehash(position)
                if position == start_slot:
                    stop = True

        return value

# 示例使用：
hash_map = HashMap(11)
hash_map.put("apple", 10)
hash_map.put("banana", 20)
hash_map.put("cherry", 30)
print(hash_map.get("apple"))  # 输出: 10
print(hash_map.get("banana"))  # 输出: 20
print(hash_map.get("cherry"))  # 输出: 30
