import heapq
from typing import List

class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        # 最小堆存三元组：(当前路径遇到的最大高度, r, c)
        min_heap = [(grid[0][0], 0, 0)]
        visited = {(0, 0)}

        while min_heap:
            max_h, r, c = heapq.heappop(min_heap)

            # 第一个弹出终点的路径，其 max_h 必然是全局最小瓶颈
            if r == n - 1 and c == n - 1:
                return max_h

            for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < n and (nr, nc) not in visited:
                    visited.add((nr, nc))
                    # 走到新格子后，这条路上的最高水位瓶颈更新为两者的较大值
                    new_max_h = max(max_h, grid[nr][nc])
                    heapq.heappush(min_heap, (new_max_h, nr, nc))