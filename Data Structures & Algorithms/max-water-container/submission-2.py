class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1
        maxWater = 0

        while left < right:
            weight = right - left
            height = min(heights[left], heights[right])
            area = height * weight
            maxWater = max(maxWater, area)

            # Greedy: 移动矮的那根
            if heights[left] < heights[right]:
                left = left + 1
            else:
                right = right - 1
            
        return maxWater

            
