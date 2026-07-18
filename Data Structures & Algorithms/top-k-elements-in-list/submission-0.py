class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}
        bucket = [[] for _ in range(len(nums) + 1)] # [[], [], []...]
        result = []
        for i in nums:
            if i in hashmap:
                hashmap[i] += 1
            else:
                hashmap[i] = 1
        
        for key,value in hashmap.items():
            bucket[value].append(key)
            
        for i in range(len(bucket)-1,0,-1):
            for num in bucket[i]:
                result.append(num)
                if len(result) == k:
                    return result