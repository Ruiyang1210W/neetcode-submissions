class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        result = []
        hashmap = {}
        majority = len(nums)//3
        for i in nums:
            if i not in hashmap:
                hashmap[i] = 1
            else:
                hashmap[i] += 1
            
            if hashmap[i] > majority:
                result.append(i)
        
        return list(set(result))

        