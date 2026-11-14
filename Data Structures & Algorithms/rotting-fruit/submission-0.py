class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        if not grid:
            return -1

        fresh = 0
        q = deque()
        row, col = len(grid), len(grid[0])

        for r in range(row):
            for c in range(col):
                if grid[r][c] == 2:
                    q.append((r,c))
                elif grid[r][c] == 1:
                    fresh += 1

        minutes = 0
        while q and fresh > 0:
            minutes += 1

            for _ in range(len(q)):
                x, y = q.popleft()
                for dx, dy in [(0,1), (1,0), (0,-1),(-1,0)]:
                    nx, ny = x+dx, y+dy
                    if 0 <= nx < row and 0 <= ny < col and grid[nx][ny] == 1:
                        fresh -= 1
                        grid[nx][ny] = 2
                        q.append((nx, ny))

        return minutes if fresh == 0 else -1


