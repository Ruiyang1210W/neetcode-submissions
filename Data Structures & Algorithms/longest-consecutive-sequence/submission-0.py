class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numbers = sorted(set(nums))
        count = 0

        for num in numbers:
            if num - 1 not in numbers:
                left = num
                temp = 1
                while left + 1 in numbers:
                    temp = temp + 1
                    left = left + 1
            
            count = max(count, temp)

        return count
                    
                

        