class Solution:
    def climbStairs(self, n: int) -> int:
        # 到第i阶的方法数 = 到第i-1阶 + 到第i-2阶
        one, two = 1, 1

        for i in range(n - 1):
            temp = one
            one = one + two
            two = temp
        
        return one
