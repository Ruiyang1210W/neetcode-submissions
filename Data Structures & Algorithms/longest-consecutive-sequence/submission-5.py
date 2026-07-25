class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # sorting
        if not nums:
            return 0
        
        res = 0 # track the longest streak
        nums.sort()

        curr, streak = nums[0],0 # curr as the first number/预测数
        i = 0 # index
        while i < len(nums):
            if curr != nums[i]: # if nums[i] doesn't match curr, reset
                curr = nums[i]
                streak = 0
            while i < len(nums) and nums[i] == curr: #吃掉所有相同的数字
                i += 1
            streak += 1
            curr += 1
            res = max(res, streak)
        
        return res
        
    