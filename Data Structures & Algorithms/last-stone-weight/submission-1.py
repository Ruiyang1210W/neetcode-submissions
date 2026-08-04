class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # 1. 取反：Python 的 heapq 默认是【小顶堆】，乘以 -1 后，最大的数会变成最小的数
        #    例如：[2, 7, 4, 1, 8, 1] -> [-2, -7, -4, -1, -8, -1]
        stones = [-s for s in stones]
        heapq.heapify(stones) #    此时堆顶 stones[0] 就是 -8（代表原本最大的石头 8

        # 3. 模拟碰撞：只要石头数量大于 1 块，就不断拿最大的两块对撞
        while len(stones) > 1:
            first = heapq.heappop(stones)
            second = heapq.heappop(stones)

            #    注意：因为都是负数，first (-8) 比 second (-7) 更小。
            #    如果 second > first（即 |-7| < |-8|，第二大的石头小于最大的石头）
            #    说明撞完后还剩下重量！
            if second > first:
                heapq.heappush(stones, first - second)
            
        # 5. 边界保护：如果所有石头刚好全部抵消，此时堆 stones 是空的。
        #    往里面 append(0) 可以防止读取 stones[0] 时报 IndexError 错误！
        stones.append(0)
        return abs(stones[0])


        