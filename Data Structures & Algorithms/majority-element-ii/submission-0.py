class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        result = []
        sorted_nums = sorted(nums)
        hashmap = {}
        majority = len(nums)//3
        for i in sorted_nums:
            if i not in hashmap:
                hashmap[i] = 1
            else:
                hashmap[i] += 1
            
            if hashmap[i] > majority:
                result.append(i)
        
        return list(set(result))

        