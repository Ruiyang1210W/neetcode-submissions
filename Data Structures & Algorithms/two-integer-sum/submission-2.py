class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        count = {}
        res = []
        for index, num in enumerate(nums):
            diff = target - num
            if diff in count:
                res = [count[diff], index]
                break
            
            count[num] = index
        
        return res

            