class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)
        nums.sort()

        for i in range(n):
            if i > 0 and nums[i] == nums[i-1]:
                continue

            left = i + 1
            right = n - 1
            
            while left < right:
                threeSum = nums[i] + nums[left] + nums[right]
                if threeSum < 0:
                    left += 1
                elif threeSum > 0:
                    right -= 1
                else:
                    res.append([nums[i], nums[left], nums[right]])

                    left += 1
                    right -= 1
                    
                    while left < right and nums[left] == nums[left-1]:
                        left += 1
                    while left < right and nums[right] == nums[right +1]:
                        right -= 1

                    
        return res