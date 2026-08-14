class Solution:
    def climbStairs(self, n: int) -> int:
        # Fiboncacci 到第i阶的方法数 = 到第i-1阶 + 到第i-2阶
        if n <= 2:
            return n
        
        a, b = 1, 2
        for _ in range(3, n + 1):
            a, b = b, a + b
        return b