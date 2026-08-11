from collections import OrderedDict

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = OrderedDict()
        

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        self.cache.move_to_end(key) # 把当前访问的 key 移到最右边（表示最近刚使用）
        return self.cache[key]

        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache.move_to_end(key)
        self.cache[key] = value

        ## 如果超出容量，弹出最左边（最久未使用）的 key
        if len(self.cache) > self.capacity:
            self.cache.popitem(last=False)
        
