class Solution:
    def majorityElement(self, nums: List[int]) -> int:      
        if len(nums) == 1:
            return nums[0]
            
        result = {}
        majority_check = len(result)/2
        
        for i in nums:
            if i not in result:
                result[i] = 1
            else:
                if result[i] >= majority_check:
                    return i
                result[i] = result[i] +1
            



                