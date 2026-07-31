class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        # minHeap with k largest integers
        self.minHeap, self.k = nums, k
        heapq.heapify(self.minHeap)
        while len(self.minHeap) > k: # 如果初始元素超过 K 个，把小的淘汰掉，直到只剩 K 个
            heapq.heappop(self.minHeap)


    def add(self, val: int) -> int:
        heapq.heappush(self.minHeap, val)
        if len(self.minHeap) > self.k: # 人数超出 K 个，淘汰堆里最小的数
            heapq.heappop(self.minHeap)
        return self.minHeap[0] # 堆顶就是第 K 大！O(1)
