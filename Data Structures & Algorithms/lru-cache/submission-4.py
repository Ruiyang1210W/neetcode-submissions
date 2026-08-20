class LRUCache:

    def __init__(self, capacity: int):
        self.d = {}
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key not in self.d:
            return -1
        
        value = self.d.pop(key, None) # 1. 拔出当前 key
        self.d[key] = value # 2. 重新塞回字典 -> 自动落到字典末尾（标记为最新访问）
        return value
        

    def put(self, key: int, value: int) -> None:
        self.d.pop(key, None) # 1. 如果已存在就先拔出（保证重新插入时能排到末尾）
        self.d[key] = value # 2. 插入新值（排在末尾）

        if len(self.d) > self.capacity:
            del self.d[next(iter(self.d))] # next(iter(self.d)) 能以 O(1) 拿到字典里的第 1 个 key（也就是最久没动过的 key）
        
