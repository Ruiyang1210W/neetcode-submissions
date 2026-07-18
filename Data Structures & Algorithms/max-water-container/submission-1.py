class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) -1
        result = 0
        while left < right:
            w = right - left
            height = min(heights[left], heights[right])
            area = w * height
            result = max(area, result)

            if heights[left] < heights[right]:
                left = left + 1
            else:
                right = right - 1

        return result