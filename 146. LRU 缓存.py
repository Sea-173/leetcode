class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.length = 0
        self.cache = {}

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        else:
            value = self.cache[key]
            del self.cache[key]
            self.cache[key] = value
            return self.cache[key]


    def put(self, key: int, value: int) -> None:
        print('self.cache', self.cache)
        if key not in self.cache:
            if self.length == self.capacity:
                del self.cache[next(iter(self.cache))]
                self.cache[key] = value
            else:
                del self.cache[key]
                self.cache[key] = value
                self.length += 1
        else:
            self.cache[key] = value
        print('self.cache', self.cache)



# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)