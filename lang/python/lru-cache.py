# https://leetcode.com/problems/lru-cache/description/

from collections import OrderedDict

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.items = OrderedDict()
        
    def get(self, key: int) -> int:
        value = -1
        if key in self.items:
            self.items.move_to_end(key)
            value = self.items[key]
        return value

    def put(self, key: int, value: int) -> None:
        if key in self.items:
            self.items.move_to_end(key)
        self.items[key] = value
        if len(self.items) > self.capacity:
            self.items.popitem(last=False)


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
