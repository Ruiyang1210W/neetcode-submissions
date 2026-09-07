class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        visit = set(deadends)
        
        if "0000" in visit:
            return -1
        # 起点恰好就是目标，0 步搞定
        if target == "0000":
            return 0


        def children(lock):
            res = []
            for i in range(4):
                # 向上拨动 (+1)
                digit = str((int(lock[i]) + 1) % 10)
                res.append(lock[:i] + digit + lock[i+1:])
                # 向下拨动 (-1)
                digit = str((int(lock[i])- 1 + 10) % 10)
                res.append(lock[:i] + digit +lock[i+1:])
            return res


        # bfs
        q = deque()
        q.append(["0000", 0]) #[lock, turns]
        visit.add("0000")
        
        while q:
            lock, turns = q.popleft()
            if lock == target:
                return turns
            for child in children(lock):
                if child not in visit:
                    visit.add(child)
                    q.append([child, turns + 1])
        return -1
