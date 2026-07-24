class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #Sorting: count the freq, sort by freq, take the top k
        freq = {}

        for num in nums:
            freq[num] = freq.get(num, 0) + 1
        
        arr = []
        for num, count in freq.items():
            arr.append([count,num]) # Python sort 只认第一个元素
        arr.sort()  # arr = [[1,99],[3, 77],[5, 88]] 

        res = []
        while len(res) < k:
            res.append(arr.pop()[1]) # 把排在最后面、频次最高的那组数据弹出来，然后我只要它的数字（[1]）
        return res


