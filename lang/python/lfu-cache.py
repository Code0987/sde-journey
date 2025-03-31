# https://leetcode.com/problems/lfu-cache/description/

from collections import defaultdict, OrderedDict

class LFUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.frequencies = defaultdict(OrderedDict)
        self.min_freq = 1

    def _update(self, key: int):
        old_freq = self.cache[key][1]
        self.frequencies[old_freq].pop(key)
        new_freq = old_freq + 1

        if not self.frequencies[old_freq]:
            self.frequencies.pop(old_freq)
            if self.min_freq == old_freq:
                self.min_freq = new_freq
        
        self.cache[key][1] = new_freq
        self.frequencies[new_freq][key] = None

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        self._update(key)
        return self.cache[key][0]

    def put(self, key: int, value: int) -> None:
        if self.capacity == 0:
            return

        if key in self.cache:
            self._update(key)
            self.cache[key][0] = value
        else:
            if len(self.cache) >= self.capacity:
                least_frequent_key, _ = self.frequencies[self.min_freq].popitem(last=False)
                self.cache.pop(least_frequent_key)
            
            self.min_freq = 1
            self.cache[key] = [value, 1]
            self.frequencies[1][key] = None

        # print('put', key, value)
        # print(self.cache)
        # for k, v in self.frequencies.items():
        #     print(k, v)
        # print()

# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
