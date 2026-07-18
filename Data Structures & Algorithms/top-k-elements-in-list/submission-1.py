class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        
        for num in nums:
            count[num] = count.get(num,0) + 1
        
        # dict 不能排序，需转成list，按照value来排序
        # count.items(): [(1,1), (2,2),(3,3)]
        # lambda x:x[1] 排序value
        sorted_counts = sorted(count.items(), key=lambda x:x[1])

        top_k = sorted_counts[-k:] #最后k个高频pair

        res = [pair[0] for pair in top_k] # Get key from pair
        return res
        