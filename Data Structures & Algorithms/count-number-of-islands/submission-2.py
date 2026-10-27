class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        row, col = len(grid), len(grid[0])
        visited = set()
        count = 0
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        # 1. dfs 必须先定义，供下方循环调用
        def dfs(r, c):
            # 必须最先检查越界，拦截所有非法坐标
            if r < 0 or r >= row or c < 0 or c >= col:
                return

            # 水域或者已访问过的陆地，直接刹车返回
            if grid[r][c] != "1" or (r, c) in visited:
                return

            visited.add((r, c))

            for dr, dc in directions:
                dfs(r + dr, c + dc)

        # 2. 遍历整张网格
        for r in range(row):
            for c in range(col):
                if grid[r][c] == "1" and (r, c) not in visited:
                    dfs(r, c)
                    count += 1

        return count