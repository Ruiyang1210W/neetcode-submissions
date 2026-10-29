class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        
        rows, cols = len(grid), len(grid[0])
        visited = set()
        

        def dfs(r,c):

            if r < 0 or r >= rows or c < 0 or c >= cols:
                return 0
            
            if grid[r][c] != 1 or (r,c) in visited:
                return 0

            visited.add((r,c))

            return 1 + dfs(r+1, c) + dfs(r, c+1) + dfs(r-1, c) + dfs(r, c-1)

        max_area = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r,c) not in visited:
                    curr_area = dfs(r,c)
                    max_area = max(curr_area, max_area)
                    

        return max_area



